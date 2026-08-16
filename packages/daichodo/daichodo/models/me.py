from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Me")


@_attrs_define
class Me:
    """
    Attributes:
        plan (str): `free`, `standard`, or `premium`
        mode (str): `live` or `test`. A `test` key reads a frozen fixture dataset, not the live registry - see
            docs/authentication.
        lookups_this_month (int): Billable lookups in the current UTC month
        capabilities (list[str]): Gated capabilities this plan includes, by name.
        included_lookups (int | None | Unset): Monthly allowance. Null means unmetered.
    """

    plan: str
    mode: str
    lookups_this_month: int
    capabilities: list[str]
    included_lookups: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plan = self.plan

        mode = self.mode

        lookups_this_month = self.lookups_this_month

        capabilities = self.capabilities

        included_lookups: int | None | Unset
        if isinstance(self.included_lookups, Unset):
            included_lookups = UNSET
        else:
            included_lookups = self.included_lookups

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "plan": plan,
                "mode": mode,
                "lookups_this_month": lookups_this_month,
                "capabilities": capabilities,
            }
        )
        if included_lookups is not UNSET:
            field_dict["included_lookups"] = included_lookups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        plan = d.pop("plan")

        mode = d.pop("mode")

        lookups_this_month = d.pop("lookups_this_month")

        capabilities = cast(list[str], d.pop("capabilities"))

        def _parse_included_lookups(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        included_lookups = _parse_included_lookups(d.pop("included_lookups", UNSET))

        me = cls(
            plan=plan,
            mode=mode,
            lookups_this_month=lookups_this_month,
            capabilities=capabilities,
            included_lookups=included_lookups,
        )

        me.additional_properties = d
        return me

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
