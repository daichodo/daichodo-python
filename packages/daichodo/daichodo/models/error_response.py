from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_response_details_type_0 import ErrorResponseDetailsType0


T = TypeVar("T", bound="ErrorResponse")


@_attrs_define
class ErrorResponse:
    """The only error body this API returns.

    Example:
        {'code': 'not_found', 'doc_url': 'https://daichodo.com/docs/errors/#not_found', 'message': 'No invoice issuer
            with registration number T1010001262216', 'request_id': 'req_01J8XZ9Q', 'type':
            'https://daichodo.com/errors/not_found'}

    Attributes:
        type_ (str): Stable URI identifying the error class
        code (str): Stable machine-readable code
        message (str): Human-readable explanation. Do not parse this.
        doc_url (str): Documentation for this error
        request_id (str): Quote this in a support request
        details (ErrorResponseDetailsType0 | None | Unset): Machine-readable specifics for codes that have them. Keys
            vary by code and are documented per code; absent entirely when there are none.
    """

    type_: str
    code: str
    message: str
    doc_url: str
    request_id: str
    details: ErrorResponseDetailsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.error_response_details_type_0 import ErrorResponseDetailsType0  # noqa: PLC0415

        type_ = self.type_

        code = self.code

        message = self.message

        doc_url = self.doc_url

        request_id = self.request_id

        details: dict[str, Any] | None | Unset
        if isinstance(self.details, Unset):
            details = UNSET
        elif isinstance(self.details, ErrorResponseDetailsType0):
            details = self.details.to_dict()
        else:
            details = self.details

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "code": code,
                "message": message,
                "doc_url": doc_url,
                "request_id": request_id,
            }
        )
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_response_details_type_0 import ErrorResponseDetailsType0  # noqa: PLC0415

        d = dict(src_dict)
        type_ = d.pop("type")

        code = d.pop("code")

        message = d.pop("message")

        doc_url = d.pop("doc_url")

        request_id = d.pop("request_id")

        def _parse_details(data: object) -> ErrorResponseDetailsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                details_type_0 = ErrorResponseDetailsType0.from_dict(data)

                return details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ErrorResponseDetailsType0 | None | Unset, data)

        details = _parse_details(d.pop("details", UNSET))

        error_response = cls(
            type_=type_,
            code=code,
            message=message,
            doc_url=doc_url,
            request_id=request_id,
            details=details,
        )

        error_response.additional_properties = d
        return error_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
