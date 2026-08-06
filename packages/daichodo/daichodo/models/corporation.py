from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Corporation")


@_attrs_define
class Corporation:
    """
    Attributes:
        corporate_number (str):
        name (None | str | Unset): Null when the NTA could not represent the name; see `has_gaiji`.
        kind (None | str | Unset): 法人種別 code
        update_date (datetime.date | None | Unset):
        change_date (datetime.date | None | Unset):
        prefecture_name (None | str | Unset):
        city_name (None | str | Unset):
        street_number (None | str | Unset):
        post_code (None | str | Unset):
        address_outside (None | str | Unset):
        has_gaiji (bool | Unset): The NTA supplied an image id instead of a character it could not represent. About 2%
            of the register. Default: False.
    """

    corporate_number: str
    name: None | str | Unset = UNSET
    kind: None | str | Unset = UNSET
    update_date: datetime.date | None | Unset = UNSET
    change_date: datetime.date | None | Unset = UNSET
    prefecture_name: None | str | Unset = UNSET
    city_name: None | str | Unset = UNSET
    street_number: None | str | Unset = UNSET
    post_code: None | str | Unset = UNSET
    address_outside: None | str | Unset = UNSET
    has_gaiji: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        corporate_number = self.corporate_number

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        kind: None | str | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        else:
            kind = self.kind

        update_date: None | str | Unset
        if isinstance(self.update_date, Unset):
            update_date = UNSET
        elif isinstance(self.update_date, datetime.date):
            update_date = self.update_date.isoformat()
        else:
            update_date = self.update_date

        change_date: None | str | Unset
        if isinstance(self.change_date, Unset):
            change_date = UNSET
        elif isinstance(self.change_date, datetime.date):
            change_date = self.change_date.isoformat()
        else:
            change_date = self.change_date

        prefecture_name: None | str | Unset
        if isinstance(self.prefecture_name, Unset):
            prefecture_name = UNSET
        else:
            prefecture_name = self.prefecture_name

        city_name: None | str | Unset
        if isinstance(self.city_name, Unset):
            city_name = UNSET
        else:
            city_name = self.city_name

        street_number: None | str | Unset
        if isinstance(self.street_number, Unset):
            street_number = UNSET
        else:
            street_number = self.street_number

        post_code: None | str | Unset
        if isinstance(self.post_code, Unset):
            post_code = UNSET
        else:
            post_code = self.post_code

        address_outside: None | str | Unset
        if isinstance(self.address_outside, Unset):
            address_outside = UNSET
        else:
            address_outside = self.address_outside

        has_gaiji = self.has_gaiji

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "corporate_number": corporate_number,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if kind is not UNSET:
            field_dict["kind"] = kind
        if update_date is not UNSET:
            field_dict["update_date"] = update_date
        if change_date is not UNSET:
            field_dict["change_date"] = change_date
        if prefecture_name is not UNSET:
            field_dict["prefecture_name"] = prefecture_name
        if city_name is not UNSET:
            field_dict["city_name"] = city_name
        if street_number is not UNSET:
            field_dict["street_number"] = street_number
        if post_code is not UNSET:
            field_dict["post_code"] = post_code
        if address_outside is not UNSET:
            field_dict["address_outside"] = address_outside
        if has_gaiji is not UNSET:
            field_dict["has_gaiji"] = has_gaiji

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        corporate_number = d.pop("corporate_number")

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kind = _parse_kind(d.pop("kind", UNSET))

        def _parse_update_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                update_date_type_0 = datetime.date.fromisoformat(data)

                return update_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        update_date = _parse_update_date(d.pop("update_date", UNSET))

        def _parse_change_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                change_date_type_0 = datetime.date.fromisoformat(data)

                return change_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        change_date = _parse_change_date(d.pop("change_date", UNSET))

        def _parse_prefecture_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prefecture_name = _parse_prefecture_name(d.pop("prefecture_name", UNSET))

        def _parse_city_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city_name = _parse_city_name(d.pop("city_name", UNSET))

        def _parse_street_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        street_number = _parse_street_number(d.pop("street_number", UNSET))

        def _parse_post_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        post_code = _parse_post_code(d.pop("post_code", UNSET))

        def _parse_address_outside(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_outside = _parse_address_outside(d.pop("address_outside", UNSET))

        has_gaiji = d.pop("has_gaiji", UNSET)

        corporation = cls(
            corporate_number=corporate_number,
            name=name,
            kind=kind,
            update_date=update_date,
            change_date=change_date,
            prefecture_name=prefecture_name,
            city_name=city_name,
            street_number=street_number,
            post_code=post_code,
            address_outside=address_outside,
            has_gaiji=has_gaiji,
        )

        corporation.additional_properties = d
        return corporation

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
