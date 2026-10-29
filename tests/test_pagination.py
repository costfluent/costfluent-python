import asyncio
import functools
import unittest
from collections.abc import Callable
from typing import Any

import httpx

from costfluent import CostfluentError, _sdk, apaginate, paginate
from costfluent.api.folders import get_folder, list_folders
from costfluent.api.teams import list_team_workspace_access
from costfluent.client import AuthenticatedClient
from costfluent.models.paginated_response_of_folder_response import PaginatedResponseOfFolderResponse

from .fake_api import BASE_URL, FakeApi, folders_page, json_response, problem

GATEWAY_URL = "https://gateway.example/costfluent"
# Each next link names the next page by its query; the path in it is the server's view of itself.
NEXT_LINKS = {
    "on another host": "http://internal-host:8080/v1/folders?workspaceId=ws_1&page={page}",
    "on the gateway's host without the prefix": "https://gateway.example/v1/folders?workspaceId=ws_1&page={page}",
    "relative": "/v1/folders?workspaceId=ws_1&page={page}",
    "carrying the prefix": GATEWAY_URL + "/v1/folders?workspaceId=ws_1&page={page}",
    "under another path": "https://gateway.example/elsewhere/v1/folders?workspaceId=ws_1&page={page}",
}
OTHER_HOST_LINK = NEXT_LINKS["on another host"]


def folder(folder_id: str) -> httpx.Response:
    return json_response(200, {"id": folder_id, "title": folder_id, "reportCount": 0})


def workspaces_page(ids: list[str], next_link: str | None) -> httpx.Response:
    return json_response(
        200,
        {
            "links": {"self": f"{BASE_URL}/v1/teams/team_1/workspaces", "next": next_link},
            "data": [{"workspaceId": ws, "workspaceName": ws, "accessLevel": "viewer"} for ws in ids],
        },
    )


def three_pages(link: str) -> FakeApi:
    return FakeApi(
        folders_page(["fld_1"], link.format(page=2)),
        folders_page(["fld_2"], link.format(page=3)),
        folders_page(["fld_3"], None),
    )


def later_urls(api: FakeApi) -> list[str]:
    return [str(request.url) for request in api.requests[1:]]


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

    def test_a_base_path_is_kept_for_every_page(self) -> None:
        for base in (GATEWAY_URL, GATEWAY_URL + "/"):
            for name, link in NEXT_LINKS.items():
                with self.subTest(base=base, link=name):
                    api = three_pages(link)

                    ids = [f.id for f in paginate(list_folders.sync, client=api.client(base), workspace_id="ws_1")]

                    self.assertEqual(ids, ["fld_1", "fld_2", "fld_3"])
                    self.assertEqual(
                        later_urls(api),
                        [
                            f"{GATEWAY_URL}/v1/folders?workspaceId=ws_1&page=2",
                            f"{GATEWAY_URL}/v1/folders?workspaceId=ws_1&page=3",
                        ],
                    )

    def test_async_pages_keep_a_base_path(self) -> None:
        for base in (GATEWAY_URL, GATEWAY_URL + "/"):
            for name, link in NEXT_LINKS.items():
                with self.subTest(base=base, link=name):
                    api = three_pages(link)

                    async def collect(api: FakeApi = api, base: str = base) -> list[str]:
                        return [
                            f.id
                            async for f in apaginate(list_folders.asyncio, client=api.client(base), workspace_id="ws_1")
                        ]

                    self.assertEqual(asyncio.run(collect()), ["fld_1", "fld_2", "fld_3"])
                    self.assertEqual(
                        later_urls(api),
                        [
                            f"{GATEWAY_URL}/v1/folders?workspaceId=ws_1&page=2",
                            f"{GATEWAY_URL}/v1/folders?workspaceId=ws_1&page=3",
                        ],
                    )

    def test_a_path_parameter_is_kept_on_every_page(self) -> None:
        # Catches page 2 dropping the base prefix, and a path rebuilt from the decoded path, which
        # would turn the encoded `/` in the team id into a path separator.
        api = FakeApi(
            workspaces_page(["ws_1"], "http://internal-host:8080/v1/teams/team%201%2Fa/workspaces?page=2"),
            workspaces_page(["ws_2"], None),
        )

        ids = [
            access.workspace_id
            for access in paginate(list_team_workspace_access.sync, client=api.client(GATEWAY_URL), team_id="team 1/a")
        ]

        self.assertEqual(ids, ["ws_1", "ws_2"])
        self.assertEqual(
            [request.url.raw_path for request in api.requests],
            [
                b"/costfluent/v1/teams/team%201%2Fa/workspaces?page=1&limit=20",
                b"/costfluent/v1/teams/team%201%2Fa/workspaces?page=2",
            ],
        )
        self.assertEqual(api.requests[1].url.host, "gateway.example")

    def test_any_callable_pages_on_the_path_it_requested(self) -> None:
        def decorated(operation: Callable[..., Any]) -> Callable[..., Any]:
            @functools.wraps(operation)
            def wrapper(*args: Any, **kwargs: Any) -> Any:
                return operation(*args, **kwargs)

            return wrapper

        class Folders:
            def list(self, **kwargs: Any) -> Any:
                return list_folders.sync(**kwargs)

        callers: dict[str, Callable[[AuthenticatedClient], tuple[Callable[..., Any], dict[str, Any]]]] = {
            "partial": lambda _: (functools.partial(list_folders.sync, workspace_id="ws_1"), {}),
            "partial binding the client": lambda client: (
                functools.partial(list_folders.sync, client=client),
                {"workspace_id": "ws_1"},
            ),
            "wraps decorator": lambda _: (decorated(list_folders.sync), {"workspace_id": "ws_1"}),
            "lambda": lambda _: (lambda **kwargs: list_folders.sync(**kwargs), {"workspace_id": "ws_1"}),
            "bound method": lambda _: (Folders().list, {"workspace_id": "ws_1"}),
        }
        for base in (BASE_URL, GATEWAY_URL):
            for name, caller in callers.items():
                with self.subTest(base=base, caller=name):
                    api = FakeApi(
                        folders_page(["fld_1"], OTHER_HOST_LINK.format(page=2)), folders_page(["fld_2"], None)
                    )
                    client = api.client(base)
                    operation, kwargs = caller(client)

                    ids = [f.id for f in paginate(operation, client=client, **kwargs)]

                    self.assertEqual(ids, ["fld_1", "fld_2"])
                    self.assertEqual(later_urls(api), [f"{base}/v1/folders?workspaceId=ws_1&page=2"])
                    self.assertEqual(api.requests[1].headers["Authorization"], api.requests[0].headers["Authorization"])

    def test_a_callers_bad_keyword_is_reported_by_the_operation(self) -> None:
        api = FakeApi()

        with self.assertRaises(TypeError) as raised:
            list(paginate(list_folders.sync, client=api.client(), workspace_id="ws_1", bogus=1))
        self.assertEqual(str(raised.exception), "sync() got an unexpected keyword argument 'bogus'")

        async def collect() -> list[str]:
            pages = apaginate(list_folders.asyncio, client=api.client(), workspace_id="ws_1", bogus=1)
            return [f.id async for f in pages]

        with self.assertRaises(TypeError) as raised:
            asyncio.run(collect())
        self.assertEqual(str(raised.exception), "asyncio() got an unexpected keyword argument 'bogus'")
        self.assertEqual(api.requests, [])

    def test_a_link_without_a_query_adds_no_question_mark(self) -> None:
        for base in (BASE_URL, GATEWAY_URL):
            with self.subTest(base=base):
                api = FakeApi(
                    folders_page(["fld_1"], "http://internal-host:8080/v1/folders"), folders_page(["fld_2"], None)
                )

                list(paginate(list_folders.sync, client=api.client(base), workspace_id="ws_1"))

                self.assertEqual(later_urls(api), [f"{base}/v1/folders"])

    def test_a_wrapper_pages_on_the_list_it_requested(self) -> None:
        with self.subTest("get, then list"):
            api = FakeApi(
                folder("fld_0"), folders_page(["fld_1"], OTHER_HOST_LINK.format(page=2)), folders_page(["fld_2"], None)
            )

            def get_then_list(**kwargs: Any) -> Any:
                get_folder.sync("fld_0", client=kwargs["client"], workspace_id="ws_1")
                return list_folders.sync(**kwargs)

            ids = [f.id for f in paginate(get_then_list, client=api.client(GATEWAY_URL), workspace_id="ws_1")]

            self.assertEqual(ids, ["fld_1", "fld_2"])
            self.assertEqual(str(api.requests[2].url), f"{GATEWAY_URL}/v1/folders?workspaceId=ws_1&page=2")

        for base in (BASE_URL, GATEWAY_URL):
            with self.subTest("list, then get", base=base):
                api = FakeApi(
                    folders_page(["fld_1"], OTHER_HOST_LINK.format(page=2)),
                    folder("fld_1"),
                    folders_page(["fld_2"], None),
                )

                def list_then_get(**kwargs: Any) -> Any:
                    page = list_folders.sync(**kwargs)
                    get_folder.sync("fld_1", client=kwargs["client"], workspace_id="ws_1")
                    return page

                ids = [f.id for f in paginate(list_then_get, client=api.client(base), workspace_id="ws_1")]

                self.assertEqual(ids, ["fld_1", "fld_2"])
                self.assertEqual(str(api.requests[2].url), f"{base}/v1/folders?workspaceId=ws_1&page=2")

        with self.subTest("two lists with the same final segment"):
            api = FakeApi(
                workspaces_page(["ws_0"], None),
                workspaces_page(["ws_1"], "http://internal-host:8080/v1/teams/team_1/workspaces?page=2"),
                workspaces_page(["ws_2"], None),
            )

            def two_lists(**kwargs: Any) -> Any:
                list_team_workspace_access.sync("team_0", **kwargs)
                return list_team_workspace_access.sync("team_1", **kwargs)

            ids = [access.workspace_id for access in paginate(two_lists, client=api.client(GATEWAY_URL))]

            self.assertEqual(ids, ["ws_1", "ws_2"])
            self.assertEqual(str(api.requests[2].url), f"{GATEWAY_URL}/v1/teams/team_1/workspaces?page=2")

    def test_a_first_page_paginate_did_not_see_follows_the_links_path(self) -> None:
        page = PaginatedResponseOfFolderResponse.from_dict(
            {
                "links": {"self": f"{BASE_URL}/v1/folders", "next": OTHER_HOST_LINK.format(page=2)},
                "data": [{"id": "fld_1", "title": "fld_1", "reportCount": 0}],
            }
        )
        api = FakeApi(folders_page(["fld_2"], None))

        ids = [f.id for f in paginate(lambda **_: page, client=api.client())]

        self.assertEqual(ids, ["fld_1", "fld_2"])
        self.assertEqual(
            [str(request.url) for request in api.requests], [f"{BASE_URL}/v1/folders?workspaceId=ws_1&page=2"]
        )

    def test_paginate_stops_listening_when_it_returns_or_raises(self) -> None:
        api = FakeApi(folders_page(["fld_1"], None), folders_page(["fld_1"], None))
        client = api.client()

        list(paginate(list_folders.sync, client=client, workspace_id="ws_1"))
        self.assertIsNone(_sdk._requested.get())

        with self.assertRaises(TypeError):
            list(paginate(list_folders.sync, client=client, workspace_id="ws_1", bogus=1))
        self.assertIsNone(_sdk._requested.get())

        async def check_async() -> None:
            # In the coroutine: asyncio.run gives its task a copy of this context, so a value left set
            # there would never be seen from the test's own.
            [f async for f in apaginate(list_folders.asyncio, client=client, workspace_id="ws_1")]
            self.assertIsNone(_sdk._requested.get())

            with self.assertRaises(TypeError):
                [f async for f in apaginate(list_folders.asyncio, client=client, workspace_id="ws_1", bogus=1)]
            self.assertIsNone(_sdk._requested.get())

        asyncio.run(check_async())

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
