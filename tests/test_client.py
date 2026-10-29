import datetime
import re
import unittest

import httpx

from costfluent import CONTRACT_SHA256, CostfluentError, __version__
from costfluent.api.cost_data import get_cost_data
from costfluent.api.folders import create_folder, get_folder
from costfluent.models.create_folder_request import CreateFolderRequest

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


class ContractTests(unittest.TestCase):
    def test_the_package_names_the_document_it_was_generated_from(self) -> None:
        self.assertIsNotNone(re.fullmatch(r"[0-9a-f]{64}", CONTRACT_SHA256))
