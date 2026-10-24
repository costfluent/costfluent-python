import asyncio
import datetime
import unittest
from unittest import mock

import httpx

from costfluent import CostfluentError, _sdk
from costfluent.api.folders import create_folder, get_folder

from .fake_api import FakeApi, json_response, problem
from .test_client import FOLDER, new_folder

FOLDER_READ = json_response(200, {"id": "fld_1", "title": "Finance", "reportCount": 0})
UNAVAILABLE = problem(503, "service_unavailable")
RATE_LIMITED = problem(429, "rate_limited", headers={"Retry-After": "7"})
NOW = datetime.datetime(2026, 10, 19, 12, 0, tzinfo=datetime.UTC)


class RetryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sleep = mock.patch.object(_sdk, "_sleep").start()
        mock.patch.object(_sdk, "_now", return_value=NOW).start()
        self.addCleanup(mock.patch.stopall)

    def post_trigger(self, api: FakeApi) -> httpx.Response:
        return api.client().get_httpx_client().post("/v1/anomalies/anm_1/acknowledge")

    def test_a_rate_limited_trigger_is_retried_after_the_wait_the_api_names(self) -> None:
        api = FakeApi(RATE_LIMITED, json_response(200, {}))

        self.assertEqual(self.post_trigger(api).status_code, 200)
        self.assertEqual(len(api.requests), 2)
        self.sleep.assert_called_once_with(7.0)

    def test_rate_limit_reset_stands_in_for_a_missing_retry_after(self) -> None:
        api = FakeApi(problem(429, "rate_limited", headers={"RateLimit-Reset": "12"}), json_response(200, {}))

        self.post_trigger(api)
        self.sleep.assert_called_once_with(12.0)

    def test_retry_after_as_an_http_date_waits_until_then(self) -> None:
        api = FakeApi(
            problem(429, "rate_limited", headers={"Retry-After": "Mon, 19 Oct 2026 12:00:30 GMT"}), FOLDER_READ
        )

        get_folder.sync(client=api.client(), folder_id="fld_1", workspace_id="ws_1")
        self.sleep.assert_called_once_with(30.0)

    def test_a_wait_over_a_minute_raises_at_once(self) -> None:
        api = FakeApi(problem(429, "rate_limited", headers={"Retry-After": "3600"}))

        with self.assertRaises(CostfluentError) as raised:
            get_folder.sync(client=api.client(), folder_id="fld_1", workspace_id="ws_1")

        self.assertTrue(raised.exception.is_rate_limited)
        self.assertEqual(len(api.requests), 1)
        self.sleep.assert_not_called()

    def test_a_read_is_retried_on_a_server_error_with_growing_backoff(self) -> None:
        api = FakeApi(UNAVAILABLE, UNAVAILABLE, UNAVAILABLE, FOLDER_READ)

        get_folder.sync(client=api.client(), folder_id="fld_1", workspace_id="ws_1")

        delays = [call.args[0] for call in self.sleep.call_args_list]
        for delay, base in zip(delays, (1.0, 2.0, 4.0), strict=True):
            self.assertTrue(base <= delay <= base * 1.25, delays)

    def test_retries_stop_after_three_and_raise_the_last_status(self) -> None:
        api = FakeApi(UNAVAILABLE, UNAVAILABLE, UNAVAILABLE, problem(502, "bad_gateway"))

        with self.assertRaises(CostfluentError) as raised:
            get_folder.sync(client=api.client(), folder_id="fld_1", workspace_id="ws_1")

        self.assertEqual(raised.exception.status, 502)
        self.assertEqual(len(api.requests), 4)

    def test_a_trigger_is_not_retried_on_a_server_error(self) -> None:
        api = FakeApi(UNAVAILABLE)

        with self.assertRaises(CostfluentError):
            self.post_trigger(api)
        self.assertEqual(len(api.requests), 1)

    def test_a_create_is_retried_under_the_same_key(self) -> None:
        api = FakeApi(UNAVAILABLE, FOLDER)

        create_folder.sync(client=api.client(), body=new_folder())

        keys = {request.headers["Idempotency-Key"] for request in api.requests}
        self.assertEqual((len(api.requests), len(keys)), (2, 1))

    def test_a_conditional_write_is_not_retried(self) -> None:
        api = FakeApi(UNAVAILABLE)

        with self.assertRaises(CostfluentError):
            api.client().get_httpx_client().put("/v1/folders/fld_1", json={}, headers={"If-Match": '"7"'})
        self.assertEqual(len(api.requests), 1)

    def test_a_lost_connection_is_retried_for_a_read_only(self) -> None:
        read = FakeApi(httpx.ConnectError("reset"), FOLDER_READ)
        get_folder.sync(client=read.client(), folder_id="fld_1", workspace_id="ws_1")
        self.assertEqual(len(read.requests), 2)

        trigger = FakeApi(httpx.ConnectError("reset"))
        with self.assertRaises(httpx.ConnectError):
            self.post_trigger(trigger)
        self.assertEqual(len(trigger.requests), 1)

    def test_a_timeout_is_not_retried(self) -> None:
        api = FakeApi(httpx.ReadTimeout("slow"))

        with self.assertRaises(httpx.ReadTimeout):
            get_folder.sync(client=api.client(), folder_id="fld_1", workspace_id="ws_1")
        self.assertEqual(len(api.requests), 1)

    def test_a_proxys_plain_404_is_retried_and_is_not_a_missing_object(self) -> None:
        edge = httpx.Response(404, content=b"404 page not found", headers={"Content-Type": "text/plain"})
        api = FakeApi(edge, edge, edge, edge)

        with self.assertRaises(CostfluentError) as raised:
            get_folder.sync(client=api.client(), folder_id="fld_1", workspace_id="ws_1")

        self.assertEqual(len(api.requests), 4)
        self.assertFalse(raised.exception.is_not_found)

    def test_the_apis_own_404_is_not_retried(self) -> None:
        api = FakeApi(problem(404, "not_found"))

        with self.assertRaises(CostfluentError):
            get_folder.sync(client=api.client(), folder_id="fld_1", workspace_id="ws_1")
        self.assertEqual(len(api.requests), 1)


class AsyncRetryTests(unittest.TestCase):
    def test_an_async_read_is_retried_like_a_sync_one(self) -> None:
        sleep = mock.AsyncMock()
        with mock.patch.object(_sdk, "_async_sleep", sleep):
            api = FakeApi(RATE_LIMITED, FOLDER_READ)
            folder = asyncio.run(get_folder.asyncio(client=api.client(), folder_id="fld_1", workspace_id="ws_1"))

        self.assertEqual(getattr(folder, "id", None), "fld_1")
        sleep.assert_awaited_once_with(7.0)

    def test_an_async_error_raises_the_typed_error(self) -> None:
        api = FakeApi(problem(404, "not_found"))

        with self.assertRaises(CostfluentError) as raised:
            asyncio.run(get_folder.asyncio(client=api.client(), folder_id="fld_9", workspace_id="ws_1"))
        self.assertTrue(raised.exception.is_not_found)
