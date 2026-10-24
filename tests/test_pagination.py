import asyncio
import unittest

from costfluent import CostfluentError, apaginate, paginate
from costfluent.api.folders import get_folder, list_folders

from .fake_api import BASE_URL, FakeApi, folders_page, json_response, problem


class PaginationTests(unittest.TestCase):
    def test_every_page_is_read_by_following_links_next(self) -> None:
        api = FakeApi(
            folders_page(["fld_1", "fld_2"], f"{BASE_URL}/v1/folders?workspaceId=ws_1&page=2&limit=2"),
            folders_page(["fld_3", "fld_4"], f"{BASE_URL}/v1/folders?workspaceId=ws_1&page=3&limit=2"),
            folders_page(["fld_5"], None),
        )

        ids = [folder.id for folder in paginate(list_folders.sync, client=api.client(), workspace_id="ws_1", limit=2)]

        self.assertEqual(ids, ["fld_1", "fld_2", "fld_3", "fld_4", "fld_5"])
        self.assertEqual(str(api.requests[2].url), f"{BASE_URL}/v1/folders?workspaceId=ws_1&page=3&limit=2")

    def test_a_link_naming_another_host_is_read_from_the_clients_own(self) -> None:
        api = FakeApi(
            folders_page(["fld_1"], "http://internal-host:8080/v1/folders?workspaceId=ws_1&page=2&limit=1"),
            folders_page(["fld_2"], None),
        )

        list(paginate(list_folders.sync, client=api.client(), workspace_id="ws_1", limit=1))

        self.assertEqual(str(api.requests[1].url), f"{BASE_URL}/v1/folders?workspaceId=ws_1&page=2&limit=1")
        self.assertEqual(api.requests[1].headers["Authorization"], api.requests[0].headers["Authorization"])

    def test_a_page_without_a_next_link_is_the_last(self) -> None:
        page = json_response(
            200, {"links": {"self": "/v1/folders"}, "data": [{"id": "fld_1", "title": "A", "reportCount": 0}]}
        )
        api = FakeApi(page)

        self.assertEqual(len(list(paginate(list_folders.sync, client=api.client(), workspace_id="ws_1"))), 1)
        self.assertEqual(len(api.requests), 1)

    def test_an_error_on_a_later_page_raises(self) -> None:
        api = FakeApi(folders_page(["fld_1"], f"{BASE_URL}/v1/folders?page=2"), problem(403, "forbidden"))

        with self.assertRaises(CostfluentError) as raised:
            list(paginate(list_folders.sync, client=api.client(), workspace_id="ws_1"))
        self.assertEqual(raised.exception.code, "forbidden")

    def test_an_operation_that_is_not_a_list_is_refused(self) -> None:
        api = FakeApi(json_response(200, {"id": "fld_1", "title": "A", "reportCount": 0}))

        with self.assertRaises(TypeError):
            list(paginate(get_folder.sync, client=api.client(), folder_id="fld_1", workspace_id="ws_1"))

    def test_async_pages_follow_the_same_links(self) -> None:
        api = FakeApi(folders_page(["fld_1"], f"{BASE_URL}/v1/folders?page=2"), folders_page(["fld_2"], None))

        async def collect() -> list[str]:
            return [
                folder.id async for folder in apaginate(list_folders.asyncio, client=api.client(), workspace_id="ws_1")
            ]

        self.assertEqual(asyncio.run(collect()), ["fld_1", "fld_2"])
