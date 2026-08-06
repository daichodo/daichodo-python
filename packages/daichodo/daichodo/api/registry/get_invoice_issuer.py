from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.invoice_issuer import InvoiceIssuer
from ...types import Response


def _get_kwargs(
    registration_number: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/invoice-issuers/{registration_number}".format(
            registration_number=quote(str(registration_number), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | InvoiceIssuer | None:
    if response.status_code == 200:
        response_200 = InvoiceIssuer.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | InvoiceIssuer]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    registration_number: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[HTTPValidationError | InvoiceIssuer]:
    """Look up a qualified invoice issuer

     Current published information for a 登録番号. Counts against your monthly quota.

    Sole traders return dates with a null `name` - that is a valid record, not a miss.

    Args:
        registration_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | InvoiceIssuer]
    """

    kwargs = _get_kwargs(
        registration_number=registration_number,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    registration_number: str,
    *,
    client: AuthenticatedClient | Client,
) -> HTTPValidationError | InvoiceIssuer | None:
    """Look up a qualified invoice issuer

     Current published information for a 登録番号. Counts against your monthly quota.

    Sole traders return dates with a null `name` - that is a valid record, not a miss.

    Args:
        registration_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | InvoiceIssuer
    """

    return sync_detailed(
        registration_number=registration_number,
        client=client,
    ).parsed


async def asyncio_detailed(
    registration_number: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[HTTPValidationError | InvoiceIssuer]:
    """Look up a qualified invoice issuer

     Current published information for a 登録番号. Counts against your monthly quota.

    Sole traders return dates with a null `name` - that is a valid record, not a miss.

    Args:
        registration_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | InvoiceIssuer]
    """

    kwargs = _get_kwargs(
        registration_number=registration_number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    registration_number: str,
    *,
    client: AuthenticatedClient | Client,
) -> HTTPValidationError | InvoiceIssuer | None:
    """Look up a qualified invoice issuer

     Current published information for a 登録番号. Counts against your monthly quota.

    Sole traders return dates with a null `name` - that is a valid record, not a miss.

    Args:
        registration_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | InvoiceIssuer
    """

    return (
        await asyncio_detailed(
            registration_number=registration_number,
            client=client,
        )
    ).parsed
