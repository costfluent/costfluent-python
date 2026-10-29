"""Against a running API: COSTFLUENT_SMOKE_BASE_URL and a COSTFLUENT_SMOKE_API_KEY that may create
workspaces, folders and providers, manage alerts and read costs. Every object it creates is named
after the run."""

import datetime
import os
import unittest
import uuid
from decimal import Decimal

from costfluent import CostfluentError, create_client, paginate
from costfluent.api.cost_alerts import create_cost_alert
from costfluent.api.cost_data import get_cost_data
from costfluent.api.custom_provider import submit_costs
from costfluent.api.folders import create_folder, get_folder, list_folders
from costfluent.api.providers import connect_provider
from costfluent.api.workspaces import create_workspace, list_workspaces
from costfluent.models.connect_provider_request import ConnectProviderRequest
from costfluent.models.connect_provider_request_credentials import ConnectProviderRequestCredentials
from costfluent.models.cost_entry import CostEntry
from costfluent.models.create_cost_alert_request import CreateCostAlertRequest
from costfluent.models.create_folder_request import CreateFolderRequest
from costfluent.models.create_workspace_request import CreateWorkspaceRequest
from costfluent.models.submit_costs_request import SubmitCostsRequest
from costfluent.models.workspace_response import WorkspaceResponse

BASE_URL = os.environ.get("COSTFLUENT_SMOKE_BASE_URL", "")
TOKEN = os.environ.get("COSTFLUENT_SMOKE_API_KEY", "")
# Three days back keeps the day inside every plan's history and apart from the TypeScript smoke's.
COST_DAY = datetime.date.today() - datetime.timedelta(days=3)
AMOUNT = "12.34567891"


@unittest.skipUnless(BASE_URL and TOKEN, "COSTFLUENT_SMOKE_BASE_URL and COSTFLUENT_SMOKE_API_KEY are not set")
class SmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.client = create_client(TOKEN, base_url=BASE_URL)
        cls.name = f"SDK smoke python {uuid.uuid4().hex[:8]}"

    def first_workspace(self) -> WorkspaceResponse:
        return next(paginate(list_workspaces.sync, client=self.client, limit=1))

    def test_workspaces_are_paged_by_links_next(self) -> None:
        created = create_workspace.sync(
            client=self.client, body=CreateWorkspaceRequest(name=self.name, currency=self.first_workspace().currency)
        )
        assert created is not None and hasattr(created, "id")

        ids = [workspace.id for workspace in paginate(list_workspaces.sync, client=self.client, limit=1)]

        self.assertGreaterEqual(len(ids), 2, "one workspace a page, so at least two pages")
        self.assertEqual(len(ids), len(set(ids)))
        self.assertIn(created.id, ids)

    def test_a_create_sent_twice_under_one_key_creates_once(self) -> None:
        workspace_id = self.first_workspace().id
        body = CreateFolderRequest(workspace_id=workspace_id, title=self.name)
        key = str(uuid.uuid4())

        first = create_folder.sync_detailed(client=self.client, body=body, idempotency_key=key)
        second = create_folder.sync_detailed(client=self.client, body=body, idempotency_key=key)

        assert first.parsed is not None and second.parsed is not None
        self.assertEqual((first.status_code, second.status_code), (201, 201))
        self.assertEqual(getattr(first.parsed, "id", None), getattr(second.parsed, "id", "replayed"))
        self.assertEqual(second.headers.get("Idempotent-Replayed"), "true")
        titles = [folder.title for folder in paginate(list_folders.sync, client=self.client, workspace_id=workspace_id)]
        self.assertEqual(titles.count(self.name), 1)

    def test_costs_read_back_as_exact_decimal_strings(self) -> None:
        currency = self.first_workspace().currency
        provider = connect_provider.sync(
            client=self.client,
            body=ConnectProviderRequest(
                key="custom", display_name=self.name, credentials=ConnectProviderRequestCredentials()
            ),
        )
        assert provider is not None and hasattr(provider, "id")
        entry = CostEntry(
            charge_period_start=COST_DAY,
            charge_category="Usage",
            service_name="sdk-smoke",
            billed_cost=AMOUNT,
            billing_currency=currency,
            line_item_id=self.name,
        )
        submitted = submit_costs.sync(provider.id, client=self.client, body=SubmitCostsRequest(costs=[entry]))
        assert submitted is not None and hasattr(submitted, "accepted_rows")
        self.assertEqual((submitted.accepted_rows, submitted.rejected_rows), (1, 0))

        costs = get_cost_data.sync(client=self.client, start_date=COST_DAY, end_date=COST_DAY)

        assert costs is not None and hasattr(costs, "data")
        amounts = [row.cost for row in costs.data]
        self.assertTrue(amounts and all(isinstance(amount, str) for amount in amounts), amounts)
        self.assertEqual(sum(Decimal(amount) for amount in amounts), Decimal(AMOUNT))

    def test_a_missing_folder_raises_the_typed_not_found_error(self) -> None:
        with self.assertRaises(CostfluentError) as raised:
            get_folder.sync("fld_AAAAAAAAAAAAAAAAAAAAAA", client=self.client, workspace_id=self.first_workspace().id)

        self.assertTrue(raised.exception.is_not_found, raised.exception)
        self.assertEqual(raised.exception.code, "not_found")

    def test_a_refused_command_names_the_field_it_refused(self) -> None:
        # The command validator refuses a percentageIncrease alert with no comparison period under the
        # detail "One or more validation errors occurred", so only the field says what to change.
        body = CreateCostAlertRequest(
            workspace_id=self.first_workspace().id,
            name=self.name,
            threshold_type="percentageIncrease",
            threshold_value="20",
        )
        with self.assertRaises(CostfluentError) as raised:
            create_cost_alert.sync(client=self.client, body=body)

        self.assertIn("comparisonPeriod", [entry.name for entry in raised.exception.field_errors], raised.exception)
        self.assertIn("comparisonPeriod: ", str(raised.exception))
