import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.validity_response import ValidityResponse
from ...types import UNSET, Response


def _get_kwargs(
    registration_number: str,
    *,
    on: datetime.date,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_on = on.isoformat()
    params["on"] = json_on

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/invoice-issuers/{registration_number}/validity".format(
            registration_number=quote(str(registration_number), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | ValidityResponse | None:
    if response.status_code == 200:
        response_200 = ValidityResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | ValidityResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    registration_number: str,
    *,
    client: AuthenticatedClient,
    on: datetime.date,
) -> Response[HTTPValidationError | ValidityResponse]:
    """Was this registration valid on a given date?

     Point-in-time validity, answered from the accumulated change log rather than current state - the
    question the official sites cannot answer.

    Requires a paid plan. Works for sole traders as well as corporations: individuals keep every date
    field, only their identity is stripped.

    Args:
        registration_number (str):
        on (datetime.date): The date to test, YYYY-MM-DD

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ValidityResponse]
    """

    kwargs = _get_kwargs(
        registration_number=registration_number,
        on=on,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    registration_number: str,
    *,
    client: AuthenticatedClient,
    on: datetime.date,
) -> HTTPValidationError | ValidityResponse | None:
    """Was this registration valid on a given date?

     Point-in-time validity, answered from the accumulated change log rather than current state - the
    question the official sites cannot answer.

    Requires a paid plan. Works for sole traders as well as corporations: individuals keep every date
    field, only their identity is stripped.

    Args:
        registration_number (str):
        on (datetime.date): The date to test, YYYY-MM-DD

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ValidityResponse
    """

    return sync_detailed(
        registration_number=registration_number,
        client=client,
        on=on,
    ).parsed


async def asyncio_detailed(
    registration_number: str,
    *,
    client: AuthenticatedClient,
    on: datetime.date,
) -> Response[HTTPValidationError | ValidityResponse]:
    """Was this registration valid on a given date?

     Point-in-time validity, answered from the accumulated change log rather than current state - the
    question the official sites cannot answer.

    Requires a paid plan. Works for sole traders as well as corporations: individuals keep every date
    field, only their identity is stripped.

    Args:
        registration_number (str):
        on (datetime.date): The date to test, YYYY-MM-DD

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ValidityResponse]
    """

    kwargs = _get_kwargs(
        registration_number=registration_number,
        on=on,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    registration_number: str,
    *,
    client: AuthenticatedClient,
    on: datetime.date,
) -> HTTPValidationError | ValidityResponse | None:
    """Was this registration valid on a given date?

     Point-in-time validity, answered from the accumulated change log rather than current state - the
    question the official sites cannot answer.

    Requires a paid plan. Works for sole traders as well as corporations: individuals keep every date
    field, only their identity is stripped.

    Args:
        registration_number (str):
        on (datetime.date): The date to test, YYYY-MM-DD

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ValidityResponse
    """

    return (
        await asyncio_detailed(
            registration_number=registration_number,
            client=client,
            on=on,
        )
    ).parsed
