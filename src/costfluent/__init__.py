"""Python client for the Costfluent Public API.

Every operation is a generated module under ``costfluent.api``, its models under
``costfluent.models``; ``create_client`` builds the client they take::

    from costfluent import create_client, paginate
    from costfluent.api.workspaces import list_workspaces

    client = create_client(token)
    for workspace in paginate(list_workspaces.sync, client=client, limit=100):
        print(workspace.name)
"""

from ._contract import CONTRACT_SHA256
from ._sdk import DEFAULT_BASE_URL, CostfluentError, apaginate, create_client, paginate
from ._version import __version__
from .client import AuthenticatedClient
from .types import UNSET, Response, Unset

__all__ = [
    "CONTRACT_SHA256",
    "DEFAULT_BASE_URL",
    "UNSET",
    "AuthenticatedClient",
    "CostfluentError",
    "Response",
    "Unset",
    "__version__",
    "apaginate",
    "create_client",
    "paginate",
]
