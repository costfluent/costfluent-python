import asyncio
import datetime
import os
import re
import socket
import unittest
from typing import NoReturn
from unittest import mock

import anyio
import httpx

import costfluent
from costfluent import CONTRACT_SHA256, CostfluentError, __version__, _sdk, create_client
from costfluent._contract import IDEMPOTENT_CREATES
from costfluent.api.cost_data import get_cost_data
from costfluent.api.cost_reports import get_cost_report_data
from costfluent.api.folders import create_folder, get_folder
from costfluent.client import AuthenticatedClient, Client
from costfluent.errors import UnexpectedStatus
from costfluent.models.create_folder_request import CreateFolderRequest
from costfluent.types import Unset

from .fake_api import TOKEN, FakeApi, json_response, problem

FOLDER = json_response(201, {"id": "fld_1", "title": "Finance"})
NIGHTLY_RUN = "nightly-2026-10-19"


def new_folder() -> CreateFolderRequest:
    return CreateFolderRequest(workspace_id="ws_1", title="Finance")


class RequestTests(unittest.TestCase):
    def test_a_request_carries_the_token_and_the_package_version(self) -> None:
        api = FakeApi(FOLDER)
        create_folder.sync(client=api.client(), body=new_folder())

        headers = api.requests[0].headers
        self.assertEqual(headers["Authorization"], f"Bearer {TOKEN}")
        self.assertEqual(headers["User-Agent"], f"costfluent-python/{__version__}")

    def test_each_create_sends_its_own_idempotency_key(self) -> None:
        api = FakeApi(FOLDER, FOLDER)
        client = api.client()
        create_folder.sync(client=client, body=new_folder())
        create_folder.sync(client=client, body=new_folder())

        keys = [request.headers["Idempotency-Key"] for request in api.requests]
        self.assertRegex(keys[0], r"^[0-9a-f-]{36}$")
        self.assertNotEqual(keys[0], keys[1])

    def test_a_callers_idempotency_key_is_sent_unchanged(self) -> None:
        api = FakeApi(FOLDER)
        create_folder.sync(client=api.client(), body=new_folder(), idempotency_key=NIGHTLY_RUN)

        self.assertEqual(api.requests[0].headers["Idempotency-Key"], NIGHTLY_RUN)

    def test_a_post_that_is_not_a_create_gets_no_key(self) -> None:
        api = FakeApi(json_response(200, {}))
        api.client().get_httpx_client().post("/v1/anomalies/anm_1/acknowledge")

        self.assertNotIn("Idempotency-Key", api.requests[0].headers)

    def test_a_create_behind_a_base_path_still_gets_a_key(self) -> None:
        api = FakeApi(FOLDER)
        create_folder.sync(client=api.client("https://gateway.example/costfluent"), body=new_folder())

        self.assertEqual(api.requests[0].url.path, "/costfluent/v1/folders")
        self.assertIn("Idempotency-Key", api.requests[0].headers)

    def test_a_create_inside_another_resource_is_matched_by_its_template(self) -> None:
        api = FakeApi(json_response(200, {}), json_response(200, {}))
        httpx_client = api.client().get_httpx_client()
        httpx_client.post("/v1/dashboards/dsh_1/widgets", json={})
        httpx_client.post("/v1/dashboards/dsh_1/duplicate", json={})

        self.assertIn("Idempotency-Key", api.requests[0].headers)
        self.assertNotIn("Idempotency-Key", api.requests[1].headers)


class BaseUrlTests(unittest.TestCase):
    """The token travels with every request, so the base URL must use https, but to this machine."""

    REFUSED = (
        "http://api.costfluent.com",
        "http://10.0.0.5:8080",
        "http://[::2]:8080",
        "HTTP://api.costfluent.com",
        "http://localhost.evil.example",
        "http://127.0.0.2",
        "ftp://api.costfluent.com",
        "api.costfluent.com",
        "https://",
    )

    def test_a_base_url_that_would_send_the_token_in_clear_is_refused_before_any_request(self) -> None:
        for base_url in self.REFUSED:
            with self.subTest(base_url):
                api = FakeApi(FOLDER)
                with self.assertRaisesRegex(ValueError, "must use https|has no host"):
                    api.client(base_url)
                self.assertEqual(api.requests, [])

    def test_the_exported_client_class_refuses_the_same_base_urls_when_built_directly(self) -> None:
        for base_url in self.REFUSED:
            with self.subTest(base_url), self.assertRaisesRegex(ValueError, "must use https|has no host"):
                costfluent.AuthenticatedClient(base_url=base_url, token=TOKEN)

    def test_the_exported_client_class_accepts_https_and_is_what_create_client_builds(self) -> None:
        client = costfluent.AuthenticatedClient(base_url="https://api.costfluent.com", token=TOKEN)
        self.assertEqual(
            client.with_headers({"X-Trace": "1"}).get_httpx_client().base_url, "https://api.costfluent.com"
        )
        self.assertIsInstance(create_client(TOKEN), costfluent.AuthenticatedClient)

    def test_https_and_plain_http_to_this_machine_are_accepted(self) -> None:
        for base_url in (
            "https://api.costfluent.com",
            "HTTPS://api.costfluent.com",
            "https://10.0.0.5:8443/costfluent",
            "http://localhost:8080",
            "http://LOCALHOST:8080",
            "http://127.0.0.1",
            "http://[::1]:8080",
        ):
            with self.subTest(base_url):
                api = FakeApi(FOLDER)
                create_folder.sync(client=api.client(base_url), body=new_folder())
                self.assertEqual(api.requests[0].headers["Authorization"], f"Bearer {TOKEN}")

    def test_the_default_base_url_is_accepted(self) -> None:
        create_client(TOKEN)

    def test_a_redirect_is_not_followed_so_the_token_never_reaches_its_target(self) -> None:
        api = FakeApi(httpx.Response(302, headers={"Location": "http://api.costfluent.com/v1/folders"}))
        with self.assertRaises(UnexpectedStatus):
            create_folder.sync(client=api.client(), body=new_folder())
        self.assertEqual([request.url.host for request in api.requests], ["api.costfluent.test"])


class ErrorTests(unittest.TestCase):
    def test_a_missing_object_raises_the_typed_not_found_error(self) -> None:
        api = FakeApi(problem(404, "not_found", detail="No folder fld_9.", traceId="00-abc-01"))

        with self.assertRaises(CostfluentError) as raised:
            get_folder.sync(client=api.client(), folder_id="fld_9", workspace_id="ws_1")

        error = raised.exception
        self.assertEqual((error.status, error.code), (404, "not_found"))
        self.assertTrue(error.is_not_found)
        self.assertEqual(error.detail, "No folder fld_9.")
        self.assertEqual(error.trace_id, "00-abc-01")
        self.assertEqual(error.request_id, "req_1")
        self.assertIn("not_found", str(error))

    def test_only_the_not_found_code_is_a_missing_object(self) -> None:
        # Another 404 the API answers, such as one for a path it does not serve, leaves the object
        # as it was: a caller that took it as gone would forget an object that still exists.
        problem_type = {"Content-Type": "application/problem+json"}
        cases = {
            "not_found": (problem(404, "not_found"), True),
            "another code": (problem(404, "operation_not_found"), False),
            "no code": (
                httpx.Response(
                    404, content=b'{"type": "about:blank", "title": "x", "status": 404}', headers=problem_type
                ),
                False,
            ),
            "a body that does not parse": (
                httpx.Response(404, content=b'{"status": 404, "code": "not_fo', headers=problem_type),
                False,
            ),
            "plain text": (
                httpx.Response(404, content=b"404 page not found", headers={"Content-Type": "text/plain"}),
                False,
            ),
        }
        for name, (response, missing) in cases.items():
            with self.subTest(name):
                with mock.patch.object(_sdk, "_sleep"):
                    api = FakeApi(*[response] * 4)

                    with self.assertRaises(CostfluentError) as raised:
                        get_folder.sync(client=api.client(), folder_id="fld_1", workspace_id="ws_1")

                self.assertEqual(raised.exception.status, 404)
                self.assertEqual(raised.exception.is_not_found, missing)

    def test_a_validation_error_carries_its_fields(self) -> None:
        api = FakeApi(
            problem(400, "validation_failed", errors=[{"name": "title", "reason": "Title must not be empty."}])
        )

        with self.assertRaises(CostfluentError) as raised:
            create_folder.sync(client=api.client(), body=CreateFolderRequest(workspace_id="ws_1", title=""))

        self.assertEqual([entry.name for entry in raised.exception.field_errors], ["title"])
        self.assertFalse(raised.exception.is_not_found)

    def test_the_message_adds_the_field_errors_the_detail_leaves_out(self) -> None:
        # The API's problems as each source writes them: the command validator's generic detail
        # beside the fields it refused, the endpoint validator's fields with no detail, and the
        # refusals whose detail already states their one entry.
        cases = {
            "command validator": (
                problem(
                    400,
                    "validation_failed",
                    detail="One or more validation errors occurred",
                    errors=[
                        {"name": "comparisonPeriod", "reason": "'comparison Period' must not be empty."},
                        {"name": "filter", "reason": "Unknown field 'cost.provider' at position 1"},
                    ],
                ),
                (
                    "One or more validation errors occurred; comparisonPeriod: 'comparison Period' must not be empty.; "
                    "filter: Unknown field 'cost.provider' at position 1"
                ),
            ),
            "endpoint validator": (
                problem(
                    400,
                    "validation_failed",
                    errors=[
                        {"name": "currency", "reason": "'Currency' must be 3 characters in length."},
                        {"name": "generalErrors", "reason": "Exactly one of amount and amountByMonth is required."},
                    ],
                ),
                "currency: 'Currency' must be 3 characters in length.; Exactly one of amount and amountByMonth is required.",
            ),
            "one handler failure": (
                problem(
                    400, "validation_failed", detail="Unknown app", errors=[{"name": "appIds", "reason": "Unknown app"}]
                ),
                "Unknown app",
            ),
            "missing capability": (
                problem(
                    403,
                    "forbidden",
                    detail="API token lacks capability: ManageTeam",
                    errors=[{"name": "capability", "reason": "manageTeam", "code": "missing_capability"}],
                ),
                "API token lacks capability: ManageTeam",
            ),
            "no detail or errors": (problem(400, "validation_failed"), "Problem"),
        }
        for name, (response, want) in cases.items():
            with self.subTest(name):
                with self.assertRaises(CostfluentError) as raised:
                    create_folder.sync(client=FakeApi(response).client(), body=new_folder())
                error = raised.exception
                self.assertEqual(str(error), f"Costfluent API answered {error.status} {error.code}: {want}")

    def test_a_reused_key_is_recognised(self) -> None:
        api = FakeApi(problem(422, "idempotency_key_reused"))

        with self.assertRaises(CostfluentError) as raised:
            create_folder.sync(client=api.client(), body=new_folder(), idempotency_key=NIGHTLY_RUN)

        self.assertTrue(raised.exception.is_idempotency_key_reused)

    def test_an_error_without_problem_details_still_raises(self) -> None:
        api = FakeApi(json_response(401, {"message": "no"}))

        with self.assertRaises(CostfluentError) as raised:
            get_folder.sync(client=api.client(), folder_id="fld_1", workspace_id="ws_1")

        self.assertEqual((raised.exception.status, raised.exception.code), (401, ""))
        self.assertIsNone(raised.exception.problem)

    def test_an_unreadable_problem_body_is_reported_as_none(self) -> None:
        # A proxy's page or a truncated answer under the problem media type.
        bodies = {
            "empty": b"",
            "html": b"<html>",
            "null": b"null",
            "no code": b'{"type": "about:blank", "title": "x", "status": 403, "retryable": false}',
        }
        for name, body in bodies.items():
            with self.subTest(name):
                api = FakeApi(
                    httpx.Response(
                        403,
                        content=body,
                        headers={"Content-Type": "application/problem+json", "X-Request-Id": "req_1"},
                    )
                )

                with self.assertRaises(CostfluentError) as raised:
                    get_folder.sync(client=api.client(), folder_id="fld_1", workspace_id="ws_1")

                error = raised.exception
                self.assertEqual((error.status, error.code, error.request_id), (403, "", "req_1"))
                self.assertIsNone(error.problem)


class MoneyTests(unittest.TestCase):
    def test_amounts_stay_the_exact_decimal_strings_the_api_sent(self) -> None:
        point = {
            "date": "2026-10-01",
            "cost": "123456789012.12345678",
            "listCost": "0.10000001",
            "amortizedCost": "-0.5",
            "currency": "EUR",
            "dimensions": {"service": "Compute"},
        }
        meta = {
            "startDate": "2026-10-01",
            "endDate": "2026-10-01",
            "granularity": "day",
            "measure": "cost",
            "totalRecords": 1,
            "presentation": {"conversions": [], "unconverted": [], "totalsByCurrency": []},
            "commitmentDiscounts": "asApplied",
            "totalCost": "123456789012.12345678",
            "dataVersion": "3f2a9c0d1e4b5a68",
        }
        api = FakeApi(json_response(200, {"links": {"self": "/v1/costs"}, "data": [point], "meta": meta}))

        costs = get_cost_data.sync(
            client=api.client(), start_date=datetime.date(2026, 10, 1), end_date=datetime.date(2026, 10, 1)
        )

        assert costs is not None and not isinstance(costs, CostfluentError)
        row = costs.data[0]
        self.assertEqual((row.cost, row.list_cost, row.amortized_cost), ("123456789012.12345678", "0.10000001", "-0.5"))
        self.assertEqual(costs.meta.total_cost, "123456789012.12345678")


class ReportDataTests(unittest.TestCase):
    def test_a_reports_data_names_the_resources_accounts_and_clusters_its_groups_key(self) -> None:
        summary = {
            "presentation": {"conversions": [], "unconverted": [], "totalsByCurrency": []},
            "measure": "cost",
            "totalsByUnit": [],
        }
        report = {
            "summary": summary,
            "series": [],
            "breakdown": [
                {"keys": ["i-0abc", "222222222222", "c-prod-eu"], "isOther": False, "cost": "12.5", "percent": 100}
            ],
            "startDate": "2026-10-01",
            "endDate": "2026-10-31",
            "resourceNames": {"i-0abc": "checkout-api"},
            "accountNames": {"222222222222": "prod-payments"},
            "clusterNames": {"c-prod-eu": "Production EU"},
        }
        api = FakeApi(json_response(200, report))

        data = get_cost_report_data.sync("rpt_1", client=api.client(), workspace_id="ws_1")

        assert data is not None and not isinstance(data, CostfluentError)
        named = (data.resource_names, data.account_names, data.cluster_names)
        self.assertEqual(
            [None if names is None or isinstance(names, Unset) else names.additional_properties for names in named],
            [{"i-0abc": "checkout-api"}, {"222222222222": "prod-payments"}, {"c-prod-eu": "Production EU"}],
        )


class ContractTests(unittest.TestCase):
    def test_the_package_names_the_document_it_was_generated_from(self) -> None:
        self.assertIsNotNone(re.fullmatch(r"[0-9a-f]{64}", CONTRACT_SHA256))

    def test_every_create_is_keyed_at_least_as_widely_as_the_go_sdk_floor(self) -> None:
        # The Go SDK's idempotency test holds the same floor; a shorter list means creates the
        # client would retry without a key, duplicating what a lost response already created.
        self.assertGreaterEqual(len(set(IDEMPOTENT_CREATES)), 18)


PROXY = "http://proxy.example:3128"
PROXY_ADDRESS = ("proxy.example", 3128)
API_ADDRESS = ("api.costfluent.com", 443)
# Plain http is accepted only to this machine, which is the one http base URL the proxy rules can see.
HTTP_BASE_URL = "http://localhost:8080"
HTTP_API_ADDRESS = ("localhost", 8080)
GATEWAY_BASE_URL = "https://gw.corp:8443"
GATEWAY_ADDRESS = ("gw.corp", 8443)


class TestEnvironmentProxy(unittest.TestCase):
    """Where the client opens its connection: the proxy the environment names for the base URL, or
    the API itself. Opening a socket is replaced by recording its address, so nothing leaves the test."""

    def setUp(self) -> None:
        # The proxy variables of the machine running the tests would decide every case otherwise.
        environment = {name: value for name, value in os.environ.items() if not name.lower().endswith("_proxy")}
        mock.patch.dict(os.environ, environment, clear=True).start()
        self.addCleanup(mock.patch.stopall)
        self.connections: list[tuple[str, int]] = []

        # httpcore opens every TCP connection through these two calls, from 0.16 (the floor httpx 0.23.1
        # brings) to 1.x; its backend classes moved and were renamed between those releases, so patching
        # them would hold the suite to one httpcore. httpcore turns the OSError into httpx.ConnectError.
        def create_connection(address: tuple[str, int], *_: object, **__: object) -> NoReturn:
            self.connections.append(address)
            raise ConnectionRefusedError("the tests open no connection")

        async def connect_tcp(remote_host: str, remote_port: int, *_: object, **__: object) -> NoReturn:
            create_connection((remote_host, remote_port))

        mock.patch.object(socket, "create_connection", create_connection).start()
        mock.patch.object(anyio, "connect_tcp", connect_tcp).start()

    def first_connection(self, environment: dict[str, str], base_url: str = _sdk.DEFAULT_BASE_URL) -> tuple[str, int]:
        with mock.patch.dict(os.environ, environment):
            client = create_client(TOKEN, base_url=base_url, max_retries=0)
            with self.assertRaises(httpx.ConnectError):
                client.get_httpx_client().get("/v1/folders")
        return self.connections.pop()

    def first_async_connection(self, environment: dict[str, str]) -> tuple[str, int]:
        with mock.patch.dict(os.environ, environment):
            client = create_client(TOKEN, max_retries=0)
            with self.assertRaises(httpx.ConnectError):
                asyncio.run(client.get_async_httpx_client().get("/v1/folders"))
        return self.connections.pop()

    def test_https_proxy_in_the_environment_is_used_for_the_api(self) -> None:
        self.assertEqual(self.first_connection({"HTTPS_PROXY": PROXY}), PROXY_ADDRESS)

    def test_the_async_client_uses_the_environment_proxy_too(self) -> None:
        self.assertEqual(self.first_async_connection({"HTTPS_PROXY": PROXY}), PROXY_ADDRESS)

    def test_all_proxy_alone_is_used(self) -> None:
        self.assertEqual(self.first_connection({"ALL_PROXY": PROXY}), PROXY_ADDRESS)

    def test_the_proxy_is_chosen_by_the_base_urls_scheme(self) -> None:
        self.assertEqual(self.first_connection({"HTTP_PROXY": PROXY}, HTTP_BASE_URL), PROXY_ADDRESS)
        self.assertEqual(self.first_connection({"HTTP_PROXY": PROXY}), API_ADDRESS)
        self.assertEqual(self.first_connection({"HTTPS_PROXY": PROXY}, HTTP_BASE_URL), HTTP_API_ADDRESS)

    def test_lower_case_variables_are_read_as_well(self) -> None:
        for name, base_url in (
            ("https_proxy", _sdk.DEFAULT_BASE_URL),
            ("http_proxy", HTTP_BASE_URL),
            ("all_proxy", _sdk.DEFAULT_BASE_URL),
        ):
            with self.subTest(name):
                self.assertEqual(self.first_connection({name: PROXY}, base_url), PROXY_ADDRESS)

    def test_a_proxy_named_without_a_scheme_is_an_http_proxy(self) -> None:
        self.assertEqual(self.first_connection({"HTTPS_PROXY": "proxy.example:3128"}), PROXY_ADDRESS)

    def test_no_proxy_covering_the_api_host_connects_directly(self) -> None:
        for name, hosts in (
            ("NO_PROXY", "api.costfluent.com"),
            ("NO_PROXY", ".costfluent.com"),
            ("NO_PROXY", "costfluent.com"),
            ("NO_PROXY", "localhost, api.costfluent.com"),
            ("NO_PROXY", "*"),
            ("no_proxy", "api.costfluent.com"),
        ):
            with self.subTest(f"{name}={hosts}"):
                self.assertEqual(self.first_connection({"HTTPS_PROXY": PROXY, name: hosts}), API_ADDRESS)
        for hosts in ("gw.corp:8443", "gw.corp", ".corp:8443"):
            with self.subTest(f"NO_PROXY={hosts} for {GATEWAY_BASE_URL}"):
                self.assertEqual(
                    self.first_connection({"HTTPS_PROXY": PROXY, "NO_PROXY": hosts}, GATEWAY_BASE_URL), GATEWAY_ADDRESS
                )
        self.assertEqual(
            self.first_async_connection({"HTTPS_PROXY": PROXY, "NO_PROXY": "api.costfluent.com"}), API_ADDRESS
        )

    def test_no_proxy_naming_other_hosts_keeps_the_proxy(self) -> None:
        for hosts in ("example.com", "notcostfluent.com", "costfluent.com.example"):
            with self.subTest(hosts):
                self.assertEqual(self.first_connection({"HTTPS_PROXY": PROXY, "NO_PROXY": hosts}), PROXY_ADDRESS)
        # An entry naming a port covers that port only.
        for hosts, base_url in (("gw.corp:9443", GATEWAY_BASE_URL), ("api.costfluent.com:8443", _sdk.DEFAULT_BASE_URL)):
            with self.subTest(f"NO_PROXY={hosts} for {base_url}"):
                self.assertEqual(
                    self.first_connection({"HTTPS_PROXY": PROXY, "NO_PROXY": hosts}, base_url), PROXY_ADDRESS
                )

    def test_a_failed_connection_to_the_proxy_is_retried(self) -> None:
        sleep = mock.patch.object(_sdk, "_sleep").start()
        async_sleep = mock.patch.object(_sdk, "_async_sleep", mock.AsyncMock()).start()
        with mock.patch.dict(os.environ, {"HTTPS_PROXY": PROXY}):
            client = create_client(TOKEN, max_retries=1)
            with self.assertRaises(httpx.ConnectError):
                client.get_httpx_client().get("/v1/folders")
            self.assertEqual(self.connections, [PROXY_ADDRESS, PROXY_ADDRESS])
            self.connections.clear()
            with self.assertRaises(httpx.ConnectError):
                asyncio.run(client.get_async_httpx_client().get("/v1/folders"))
            self.assertEqual(self.connections, [PROXY_ADDRESS, PROXY_ADDRESS])

        sleep.assert_called_once()
        async_sleep.assert_awaited_once()

    def test_an_explicit_transport_still_replaces_the_proxy(self) -> None:
        sleep = mock.patch.object(_sdk, "_sleep").start()
        api = FakeApi(problem(503, "service_unavailable"), json_response(200, {}))
        with mock.patch.dict(os.environ, {"HTTPS_PROXY": PROXY}):
            response = api.client().get_httpx_client().get("/v1/folders/fld_1")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(api.requests), 2)
        sleep.assert_called_once()
        self.assertEqual(self.connections, [])

    def test_a_proxy_in_an_explicit_transport_wins_over_the_environment(self) -> None:
        with mock.patch.dict(os.environ, {"HTTPS_PROXY": PROXY}):
            client = create_client(
                TOKEN, transport=httpx.HTTPTransport(proxy=httpx.Proxy("http://chosen.example:8080")), max_retries=0
            )
            with self.assertRaises(httpx.ConnectError):
                client.get_httpx_client().get("/v1/folders")

        self.assertEqual(self.connections, [("chosen.example", 8080)])


class ClientReprTests(unittest.TestCase):
    """A client's repr and str reach tracebacks, logs and error trackers, so neither may carry the token."""

    SECRET = "token-under-test"
    REPR_BASE_URL = "https://api.costfluent.test"

    def assert_hides_the_token(self, client: object) -> None:
        for text in (repr(client), str(client), f"{client}"):
            self.assertNotIn(self.SECRET, text)
        self.assertIn(self.REPR_BASE_URL, repr(client))

    def test_the_client_create_client_returns_hides_the_token(self) -> None:
        client = create_client(self.SECRET, base_url=self.REPR_BASE_URL)
        self.assert_hides_the_token(client)
        client.get_httpx_client()
        client.get_async_httpx_client()
        self.assert_hides_the_token(client)

    def test_the_clients_the_builders_return_hide_the_token(self) -> None:
        client = create_client(self.SECRET, base_url=self.REPR_BASE_URL)
        self.assert_hides_the_token(client.with_headers({"X-Trace": "1"}))
        self.assert_hides_the_token(client.with_cookies({"session": "1"}))
        self.assert_hides_the_token(client.with_timeout(httpx.Timeout(5.0)))

    def test_a_directly_built_client_hides_the_token_before_and_after_it_builds_its_httpx_clients(self) -> None:
        for prefix in ("Bearer", ""):
            with self.subTest(prefix=prefix):
                client = AuthenticatedClient(base_url=self.REPR_BASE_URL, token=self.SECRET, prefix=prefix)
                self.assert_hides_the_token(client)
                client.get_httpx_client()
                self.assert_hides_the_token(client)
                self.assert_hides_the_token(client.with_headers({"X-Trace": "1"}))

    def test_a_directly_built_client_hides_the_token_after_it_builds_its_async_client(self) -> None:
        client = AuthenticatedClient(base_url=self.REPR_BASE_URL, token=self.SECRET)
        client.get_async_httpx_client()
        self.assert_hides_the_token(client)

    def test_a_plain_client_given_the_token_as_a_header_hides_it(self) -> None:
        client = Client(base_url=self.REPR_BASE_URL, headers={"Authorization": f"Bearer {self.SECRET}"})
        self.assert_hides_the_token(client)
        client.get_httpx_client()
        self.assert_hides_the_token(client.with_timeout(httpx.Timeout(5.0)))
