from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.kubernetes_report import KubernetesReport
from ...models.kubernetes_report_accepted_response import (
    KubernetesReportAcceptedResponse,
)
from ...types import Response


def _get_kwargs(
    *,
    body: KubernetesReport,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/kubernetes/reports",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | KubernetesReportAcceptedResponse | None:
    if response.status_code == 202:
        response_202 = KubernetesReportAcceptedResponse.from_dict(response.json())

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

    if response.status_code == 409:
        response_409 = ApiError.from_dict(response.json())

        return response_409

    if response.status_code == 410:
        response_410 = ApiError.from_dict(response.json())

        return response_410

    if response.status_code == 413:
        response_413 = ApiError.from_dict(response.json())

        return response_413

    if response.status_code == 415:
        response_415 = ApiError.from_dict(response.json())

        return response_415

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
) -> Response[ApiError | KubernetesReportAcceptedResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: KubernetesReport,
) -> Response[ApiError | KubernetesReportAcceptedResponse]:
    """Report Kubernetes usage

     Accepts one aggregated window from the Costfluent Kubernetes agent, as JSON, gzip-compressed with
    Content-Encoding: gzip, with the token of the cluster it reports for. A cluster is added in
    Costfluent before its first report, and its token reports for it alone: another cluster_id, or any
    token that is not a cluster token, is refused with 403. A schema_version this API does not read,
    newer than it knows or retired, is answered 422 rather than refused as invalid, so the agent keeps
    the report and retries it.

    Needs an organization token with `reportKubernetesUsage`.

    Args:
        body (KubernetesReport):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | KubernetesReportAcceptedResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: KubernetesReport,
) -> ApiError | KubernetesReportAcceptedResponse | None:
    """Report Kubernetes usage

     Accepts one aggregated window from the Costfluent Kubernetes agent, as JSON, gzip-compressed with
    Content-Encoding: gzip, with the token of the cluster it reports for. A cluster is added in
    Costfluent before its first report, and its token reports for it alone: another cluster_id, or any
    token that is not a cluster token, is refused with 403. A schema_version this API does not read,
    newer than it knows or retired, is answered 422 rather than refused as invalid, so the agent keeps
    the report and retries it.

    Needs an organization token with `reportKubernetesUsage`.

    Args:
        body (KubernetesReport):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | KubernetesReportAcceptedResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: KubernetesReport,
) -> Response[ApiError | KubernetesReportAcceptedResponse]:
    """Report Kubernetes usage

     Accepts one aggregated window from the Costfluent Kubernetes agent, as JSON, gzip-compressed with
    Content-Encoding: gzip, with the token of the cluster it reports for. A cluster is added in
    Costfluent before its first report, and its token reports for it alone: another cluster_id, or any
    token that is not a cluster token, is refused with 403. A schema_version this API does not read,
    newer than it knows or retired, is answered 422 rather than refused as invalid, so the agent keeps
    the report and retries it.

    Needs an organization token with `reportKubernetesUsage`.

    Args:
        body (KubernetesReport):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | KubernetesReportAcceptedResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: KubernetesReport,
) -> ApiError | KubernetesReportAcceptedResponse | None:
    """Report Kubernetes usage

     Accepts one aggregated window from the Costfluent Kubernetes agent, as JSON, gzip-compressed with
    Content-Encoding: gzip, with the token of the cluster it reports for. A cluster is added in
    Costfluent before its first report, and its token reports for it alone: another cluster_id, or any
    token that is not a cluster token, is refused with 403. A schema_version this API does not read,
    newer than it knows or retired, is answered 422 rather than refused as invalid, so the agent keeps
    the report and retries it.

    Needs an organization token with `reportKubernetesUsage`.

    Args:
        body (KubernetesReport):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | KubernetesReportAcceptedResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
