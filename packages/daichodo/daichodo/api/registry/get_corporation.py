from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.corporation import Corporation
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    corporate_number: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/corporations/{corporate_number}".format(
            corporate_number=quote(str(corporate_number), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Corporation | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = Corporation.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Corporation | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    corporate_number: str,
    *,
    client: AuthenticatedClient,
) -> Response[Corporation | ErrorResponse]:
    """Look up a corporate number

     Current published information for a 法人番号. Counts against your quota.

    Args:
        corporate_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Corporation | ErrorResponse]
    """

    kwargs = _get_kwargs(
        corporate_number=corporate_number,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    corporate_number: str,
    *,
    client: AuthenticatedClient,
) -> Corporation | ErrorResponse | None:
    """Look up a corporate number

     Current published information for a 法人番号. Counts against your quota.

    Args:
        corporate_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Corporation | ErrorResponse
    """

    return sync_detailed(
        corporate_number=corporate_number,
        client=client,
    ).parsed


async def asyncio_detailed(
    corporate_number: str,
    *,
    client: AuthenticatedClient,
) -> Response[Corporation | ErrorResponse]:
    """Look up a corporate number

     Current published information for a 法人番号. Counts against your quota.

    Args:
        corporate_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Corporation | ErrorResponse]
    """

    kwargs = _get_kwargs(
        corporate_number=corporate_number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    corporate_number: str,
    *,
    client: AuthenticatedClient,
) -> Corporation | ErrorResponse | None:
    """Look up a corporate number

     Current published information for a 法人番号. Counts against your quota.

    Args:
        corporate_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Corporation | ErrorResponse
    """

    return (
        await asyncio_detailed(
            corporate_number=corporate_number,
            client=client,
        )
    ).parsed
