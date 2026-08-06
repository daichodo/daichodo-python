from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceIssuer")


@_attrs_define
class InvoiceIssuer:
    """
    Attributes:
        registration_number (str):
        corporate_number (None | str | Unset): Null for sole traders, whose numbers are not derived from a 法人番号.
        kind (None | str | Unset): `corporate` or `individual`
        country (None | str | Unset):
        registration_date (datetime.date | None | Unset):
        update_date (datetime.date | None | Unset):
        disposal_date (datetime.date | None | Unset): 取消年月日
        expire_date (datetime.date | None | Unset): 失効年月日
        name (None | str | Unset): **Null for sole traders.** The NTA strips identity fields for individuals at source,
            and they are roughly half the register. A null name means the record exists and has no published name - it does
            NOT mean the number is unregistered.
        kana (None | str | Unset):
        address (None | str | Unset):
        trade_name (None | str | Unset): 主たる屋号
    """

    registration_number: str
    corporate_number: None | str | Unset = UNSET
    kind: None | str | Unset = UNSET
    country: None | str | Unset = UNSET
    registration_date: datetime.date | None | Unset = UNSET
    update_date: datetime.date | None | Unset = UNSET
    disposal_date: datetime.date | None | Unset = UNSET
    expire_date: datetime.date | None | Unset = UNSET
    name: None | str | Unset = UNSET
    kana: None | str | Unset = UNSET
    address: None | str | Unset = UNSET
    trade_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        registration_number = self.registration_number

        corporate_number: None | str | Unset
        if isinstance(self.corporate_number, Unset):
            corporate_number = UNSET
        else:
            corporate_number = self.corporate_number

        kind: None | str | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        else:
            kind = self.kind

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        registration_date: None | str | Unset
        if isinstance(self.registration_date, Unset):
            registration_date = UNSET
        elif isinstance(self.registration_date, datetime.date):
            registration_date = self.registration_date.isoformat()
        else:
            registration_date = self.registration_date

        update_date: None | str | Unset
        if isinstance(self.update_date, Unset):
            update_date = UNSET
        elif isinstance(self.update_date, datetime.date):
            update_date = self.update_date.isoformat()
        else:
            update_date = self.update_date

        disposal_date: None | str | Unset
        if isinstance(self.disposal_date, Unset):
            disposal_date = UNSET
        elif isinstance(self.disposal_date, datetime.date):
            disposal_date = self.disposal_date.isoformat()
        else:
            disposal_date = self.disposal_date

        expire_date: None | str | Unset
        if isinstance(self.expire_date, Unset):
            expire_date = UNSET
        elif isinstance(self.expire_date, datetime.date):
            expire_date = self.expire_date.isoformat()
        else:
            expire_date = self.expire_date

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        kana: None | str | Unset
        if isinstance(self.kana, Unset):
            kana = UNSET
        else:
            kana = self.kana

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        trade_name: None | str | Unset
        if isinstance(self.trade_name, Unset):
            trade_name = UNSET
        else:
            trade_name = self.trade_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "registration_number": registration_number,
            }
        )
        if corporate_number is not UNSET:
            field_dict["corporate_number"] = corporate_number
        if kind is not UNSET:
            field_dict["kind"] = kind
        if country is not UNSET:
            field_dict["country"] = country
        if registration_date is not UNSET:
            field_dict["registration_date"] = registration_date
        if update_date is not UNSET:
            field_dict["update_date"] = update_date
        if disposal_date is not UNSET:
            field_dict["disposal_date"] = disposal_date
        if expire_date is not UNSET:
            field_dict["expire_date"] = expire_date
        if name is not UNSET:
            field_dict["name"] = name
        if kana is not UNSET:
            field_dict["kana"] = kana
        if address is not UNSET:
            field_dict["address"] = address
        if trade_name is not UNSET:
            field_dict["trade_name"] = trade_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        registration_number = d.pop("registration_number")

        def _parse_corporate_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        corporate_number = _parse_corporate_number(d.pop("corporate_number", UNSET))

        def _parse_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kind = _parse_kind(d.pop("kind", UNSET))

        def _parse_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country = _parse_country(d.pop("country", UNSET))

        def _parse_registration_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                registration_date_type_0 = datetime.date.fromisoformat(data)

                return registration_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        registration_date = _parse_registration_date(d.pop("registration_date", UNSET))

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

        def _parse_disposal_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                disposal_date_type_0 = datetime.date.fromisoformat(data)

                return disposal_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        disposal_date = _parse_disposal_date(d.pop("disposal_date", UNSET))

        def _parse_expire_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expire_date_type_0 = datetime.date.fromisoformat(data)

                return expire_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        expire_date = _parse_expire_date(d.pop("expire_date", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_kana(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kana = _parse_kana(d.pop("kana", UNSET))

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))

        def _parse_trade_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trade_name = _parse_trade_name(d.pop("trade_name", UNSET))

        invoice_issuer = cls(
            registration_number=registration_number,
            corporate_number=corporate_number,
            kind=kind,
            country=country,
            registration_date=registration_date,
            update_date=update_date,
            disposal_date=disposal_date,
            expire_date=expire_date,
            name=name,
            kana=kana,
            address=address,
            trade_name=trade_name,
        )

        invoice_issuer.additional_properties = d
        return invoice_issuer

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
