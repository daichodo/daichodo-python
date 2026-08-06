from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ValidityResponse")


@_attrs_define
class ValidityResponse:
    """
    Attributes:
        registration_number (str):
        on (datetime.date):
        valid (bool):
        reason (str): `valid`, `not_yet_registered`, or `registration_ended`
        registered_on (datetime.date | None | Unset):
        ended_on (datetime.date | None | Unset):
    """

    registration_number: str
    on: datetime.date
    valid: bool
    reason: str
    registered_on: datetime.date | None | Unset = UNSET
    ended_on: datetime.date | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        registration_number = self.registration_number

        on = self.on.isoformat()

        valid = self.valid

        reason = self.reason

        registered_on: None | str | Unset
        if isinstance(self.registered_on, Unset):
            registered_on = UNSET
        elif isinstance(self.registered_on, datetime.date):
            registered_on = self.registered_on.isoformat()
        else:
            registered_on = self.registered_on

        ended_on: None | str | Unset
        if isinstance(self.ended_on, Unset):
            ended_on = UNSET
        elif isinstance(self.ended_on, datetime.date):
            ended_on = self.ended_on.isoformat()
        else:
            ended_on = self.ended_on

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "registration_number": registration_number,
                "on": on,
                "valid": valid,
                "reason": reason,
            }
        )
        if registered_on is not UNSET:
            field_dict["registered_on"] = registered_on
        if ended_on is not UNSET:
            field_dict["ended_on"] = ended_on

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        registration_number = d.pop("registration_number")

        on = datetime.date.fromisoformat(d.pop("on"))

        valid = d.pop("valid")

        reason = d.pop("reason")

        def _parse_registered_on(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                registered_on_type_0 = datetime.date.fromisoformat(data)

                return registered_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        registered_on = _parse_registered_on(d.pop("registered_on", UNSET))

        def _parse_ended_on(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ended_on_type_0 = datetime.date.fromisoformat(data)

                return ended_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        ended_on = _parse_ended_on(d.pop("ended_on", UNSET))

        validity_response = cls(
            registration_number=registration_number,
            on=on,
            valid=valid,
            reason=reason,
            registered_on=registered_on,
            ended_on=ended_on,
        )

        validity_response.additional_properties = d
        return validity_response

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
