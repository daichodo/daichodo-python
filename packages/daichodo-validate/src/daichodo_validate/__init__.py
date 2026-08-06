"""Validate Japanese corporate numbers (法人番号) and qualified invoice
registration numbers (登録番号).

Zero dependencies, no network, no API key. The check-digit rules come from the
National Tax Agency's published specification, so this needs no service behind
it — which is why it is given away.

It tells you whether a number is **well-formed**, not whether it is
**registered**. For that you need a lookup: https://daichodo.com

This is a copy of the implementation the Daichodo API runs, not a
reimplementation. Both assert against the same `check-digit-vectors.json`, so
the two cannot drift apart without a test failing on one side or the other.
"""
from __future__ import annotations

import re
from dataclasses import dataclass

CORPORATE_NUMBER = re.compile(r"^\d{13}$")
REGISTRATION_NUMBER = re.compile(r"^T\d{13}$")


@dataclass(frozen=True)
class ValidationResult:
    value: str
    valid: bool
    reason: str | None = None
    corporate_number: str | None = None

    def as_dict(self) -> dict:
        return {
            "value": self.value,
            "valid": self.valid,
            "reason": self.reason,
            "corporate_number": self.corporate_number,
        }


def check_digit(base: str) -> int:
    """Compute the 法人番号 check digit for a 12-digit base.

    Per the NTA specification:

        検査用数字 = 9 - (Σ(n=1..12) Pn × Qn) mod 9

    where `Pn` is the nth digit counting from the RIGHT of the 12-digit body,
    and `Qn` is 1 for odd n and 2 for even n.

    The right-to-left ordering is the part that is easy to get backwards, and a
    reversed implementation still produces a plausible digit for roughly one
    number in nine — so it passes casual testing and fails in production.
    """
    if len(base) != 12 or not base.isdigit():
        raise ValueError("check digit is computed over exactly 12 digits")

    total = sum(
        int(digit) * (2 if (index + 1) % 2 == 0 else 1)
        for index, digit in enumerate(reversed(base))
    )
    return 9 - (total % 9)


def validate_corporate_number(value: str) -> ValidationResult:
    """Validate a 13-digit 法人番号, including its check digit."""
    cleaned = _clean(value)

    if not CORPORATE_NUMBER.match(cleaned):
        return ValidationResult(value, False, "must be exactly 13 digits")

    expected = check_digit(cleaned[1:])
    if int(cleaned[0]) != expected:
        return ValidationResult(
            value, False, f"check digit is {cleaned[0]}, expected {expected}"
        )

    return ValidationResult(value, True, corporate_number=cleaned)


def validate_registration_number(value: str) -> ValidationResult:
    """Validate a 適格請求書発行事業者 登録番号 (`T` + 13 digits).

    For corporations the 13 digits are the 法人番号, so the check digit applies.
    Individuals are assigned a number that is not derived from a 法人番号 and
    carries no verifiable check digit — format is all that can be asserted, and
    claiming otherwise would reject roughly half the register.
    """
    cleaned = _clean(value).upper()

    if not REGISTRATION_NUMBER.match(cleaned):
        return ValidationResult(value, False, "must be 'T' followed by 13 digits")

    body = cleaned[1:]
    expected = check_digit(body[1:])
    if int(body[0]) == expected:
        return ValidationResult(value, True, corporate_number=body)

    # Format-valid but not a corporate number. Sole traders live here, so this
    # is not an error — only an absence of a corporate number to join on.
    return ValidationResult(value, True, reason="not derived from a 法人番号")


def _clean(value: str) -> str:
    """Strip the separators people paste from invoices and spreadsheets."""
    return re.sub(r"[\s\-‐－ー―]", "", value.strip())


__all__ = [
    "ValidationResult",
    "check_digit",
    "validate_corporate_number",
    "validate_registration_number",
    "is_valid",
]


def is_valid(value: str) -> bool:
    """True if the value is a well-formed number of either kind."""
    cleaned = _clean(value).upper()
    checker = (
        validate_registration_number
        if cleaned.startswith("T")
        else validate_corporate_number
    )
    return checker(value).valid
