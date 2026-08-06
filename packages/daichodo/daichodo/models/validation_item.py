from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ValidationItem")


@_attrs_define
class ValidationItem:
    """
    Attributes:
        value (str): The number as supplied, unmodified
        valid (bool):
        reason (None | str | Unset): Why the number is invalid, or a note qualifying a valid result. Present on some
            valid results - a registration number that is format-valid but not derived from a 法人番号 is a sole trader, not an
            error.
        corporate_number (None | str | Unset): The 13-digit 法人番号 this number corresponds to, when it has one. Null for
            sole traders, whose registration numbers are not derived from a corporate number.
    """

    value: str
    valid: bool
    reason: None | str | Unset = UNSET
    corporate_number: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        valid = self.valid

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        corporate_number: None | str | Unset
        if isinstance(self.corporate_number, Unset):
            corporate_number = UNSET
        else:
            corporate_number = self.corporate_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
                "valid": valid,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason
        if corporate_number is not UNSET:
            field_dict["corporate_number"] = corporate_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value")

        valid = d.pop("valid")

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        def _parse_corporate_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        corporate_number = _parse_corporate_number(d.pop("corporate_number", UNSET))

        validation_item = cls(
            value=value,
            valid=valid,
            reason=reason,
            corporate_number=corporate_number,
        )

        validation_item.additional_properties = d
        return validation_item

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
