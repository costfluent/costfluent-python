from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.custom_cost_upload_response import CustomCostUploadResponse
from ...models.upload_custom_costs_request import UploadCustomCostsRequest
from ...types import Response


def _get_kwargs(
    provider_id: str,
    *,
    body: UploadCustomCostsRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/custom-providers/{provider_id}/uploads".format(
            provider_id=quote(str(provider_id), safe=""),
        ),
    }

    _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | CustomCostUploadResponse | None:
    if response.status_code == 202:
        response_202 = CustomCostUploadResponse.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = ApiError.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ApiError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ApiError.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ApiError.from_dict(response.json())

        return response_404

    if response.status_code == 408:
        response_408 = ApiError.from_dict(response.json())

        return response_408

    if response.status_code == 413:
        response_413 = ApiError.from_dict(response.json())

        return response_413

    if response.status_code == 422:
        response_422 = ApiError.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = ApiError.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ApiError.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ApiError.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiError | CustomCostUploadResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    provider_id: str,
    *,
    client: AuthenticatedClient,
    body: UploadCustomCostsRequest,
) -> Response[ApiError | CustomCostUploadResponse]:
    """Upload cost files

     Uploads one run of a FOCUS cost export to a custom provider: every file of the run in a repeated
    multipart field `file`, each .csv or .csv.gz with the same header, up to 90 MB together. The upload
    is accepted as pending and processed in the background; if any row is invalid nothing is committed
    and the upload fails with its errors. A completed upload replaces the provider's cost for every day
    from its first charge to its last. Its rows count toward the organization's monthly volume, one row
    for each day a cost is spread over, and the upload is checked whole before any day is committed: one
    that would pass a monthly volume limit set for the organization, or is processed while ingestion is
    paused, fails and commits nothing.

    Needs an organization token with `manageProviders`.

    Args:
        provider_id (str):
        body (UploadCustomCostsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | CustomCostUploadResponse]
    """

    kwargs = _get_kwargs(
        provider_id=provider_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    provider_id: str,
    *,
    client: AuthenticatedClient,
    body: UploadCustomCostsRequest,
) -> ApiError | CustomCostUploadResponse | None:
    """Upload cost files

     Uploads one run of a FOCUS cost export to a custom provider: every file of the run in a repeated
    multipart field `file`, each .csv or .csv.gz with the same header, up to 90 MB together. The upload
    is accepted as pending and processed in the background; if any row is invalid nothing is committed
    and the upload fails with its errors. A completed upload replaces the provider's cost for every day
    from its first charge to its last. Its rows count toward the organization's monthly volume, one row
    for each day a cost is spread over, and the upload is checked whole before any day is committed: one
    that would pass a monthly volume limit set for the organization, or is processed while ingestion is
    paused, fails and commits nothing.

    Needs an organization token with `manageProviders`.

    Args:
        provider_id (str):
        body (UploadCustomCostsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | CustomCostUploadResponse
    """

    return sync_detailed(
        provider_id=provider_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    provider_id: str,
    *,
    client: AuthenticatedClient,
    body: UploadCustomCostsRequest,
) -> Response[ApiError | CustomCostUploadResponse]:
    """Upload cost files

     Uploads one run of a FOCUS cost export to a custom provider: every file of the run in a repeated
    multipart field `file`, each .csv or .csv.gz with the same header, up to 90 MB together. The upload
    is accepted as pending and processed in the background; if any row is invalid nothing is committed
    and the upload fails with its errors. A completed upload replaces the provider's cost for every day
    from its first charge to its last. Its rows count toward the organization's monthly volume, one row
    for each day a cost is spread over, and the upload is checked whole before any day is committed: one
    that would pass a monthly volume limit set for the organization, or is processed while ingestion is
    paused, fails and commits nothing.

    Needs an organization token with `manageProviders`.

    Args:
        provider_id (str):
        body (UploadCustomCostsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | CustomCostUploadResponse]
    """

    kwargs = _get_kwargs(
        provider_id=provider_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    provider_id: str,
    *,
    client: AuthenticatedClient,
    body: UploadCustomCostsRequest,
) -> ApiError | CustomCostUploadResponse | None:
    """Upload cost files

     Uploads one run of a FOCUS cost export to a custom provider: every file of the run in a repeated
    multipart field `file`, each .csv or .csv.gz with the same header, up to 90 MB together. The upload
    is accepted as pending and processed in the background; if any row is invalid nothing is committed
    and the upload fails with its errors. A completed upload replaces the provider's cost for every day
    from its first charge to its last. Its rows count toward the organization's monthly volume, one row
    for each day a cost is spread over, and the upload is checked whole before any day is committed: one
    that would pass a monthly volume limit set for the organization, or is processed while ingestion is
    paused, fails and commits nothing.

    Needs an organization token with `manageProviders`.

    Args:
        provider_id (str):
        body (UploadCustomCostsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | CustomCostUploadResponse
    """

    return (
        await asyncio_detailed(
            provider_id=provider_id,
            client=client,
            body=body,
        )
    ).parsed
