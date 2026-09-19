"""Validation, including the cross-language check-digit contract.

`check-digit-vectors.json` is shared byte-for-byte with the Daichodo API and
with `@daichodo/validate` in TypeScript. They are the same algorithm implemented
separately; a divergence would mean this package rejecting numbers the API
accepts, and a customer trusting the local answer without ever making the
request.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from daichodo_validate import (
    check_digit,
    is_valid,
    validate_corporate_number,
    validate_registration_number,
)

VECTORS = json.loads(
    (Path(__file__).parent / "check-digit-vectors.json").read_text(encoding="utf-8")
)

# Real 法人番号, from published NTA data rather than invented.
REAL = ["1010001153225", "1010001262216", "1010001262934", "1090001018602"]


def test_the_vector_set_is_substantial():
    # A truncated file would make the check below pass while proving nothing.
    assert len(VECTORS["cases"]) > 500
    assert any(case.get("note") for case in VECTORS["cases"])


def test_every_shared_vector_matches():
    mismatches = [
        c["body"] for c in VECTORS["cases"] if check_digit(c["body"]) != c["digit"]
    ]
    assert not mismatches, f"{len(mismatches)} divergences, first: {mismatches[:3]}"


def test_every_digit_position_is_covered():
    # A weighting bug in one position is the realistic failure, and random
    # coverage averages it away.
    bodies = {c["body"] for c in VECTORS["cases"]}
    for position in range(12):
        probe = ["0"] * 12
        probe[position] = "7"
        assert "".join(probe) in bodies


@pytest.mark.parametrize("number", REAL)
def test_real_numbers_validate(number):
    assert validate_corporate_number(number).valid


def test_digit_weighting_is_right_to_left():
    assert check_digit("010001153225") == 1
    assert check_digit("522351100010") != 1


def test_a_flipped_check_digit_is_rejected():
    result = validate_corporate_number("2010001153225")
    assert not result.valid
    assert "check digit" in result.reason


def test_a_failed_check_digit_is_rejected_sole_trader_or_not():
    """The branch the shared vectors do not cover, and this is why it exists.

    Until 0.2.0 this asserted the opposite - that T1234567890123 was VALID,
    excused as a sole trader. The premise was measured false: all 5,421,496
    numbers in the register satisfy the check digit, corporations, sole traders
    and 人格のない社団等 alike. So the escape hatch protected nothing real and
    admitted every typo and every fabrication.

    The test pinning that behaviour is exactly why the drift went unnoticed.
    check-digit-vectors.json is shared with the API and the TypeScript package
    and covers `check_digit` alone - the arithmetic - so when the other two
    started rejecting these on 2026-09-05, every shared vector still passed
    here. Green tests on both sides, opposite answers from the same input, for
    two weeks. Assert behaviour, not just arithmetic.
    """
    fabricated = validate_registration_number("T1234567890123")
    assert not fabricated.valid
    assert fabricated.reason == "check digit is 1, expected 9"
    assert fabricated.corporate_number is None

    # A one-digit typo of a real number, which is the common case in the wild.
    typo = validate_registration_number("T1010001153226")
    assert not typo.valid
    assert "check digit" in typo.reason


def test_the_t_prefix_does_not_change_the_verdict():
    """The old bug's sharpest edge: the SAME digits disagreed with themselves.

    T1234567890123 returned valid while 1234567890123 was correctly rejected,
    because only the registration-number path carried the escape hatch.
    """
    assert validate_registration_number("T1234567890123").valid is False
    assert validate_corporate_number("1234567890123").valid is False
    assert is_valid("T1234567890123") is False
    assert is_valid("1234567890123") is False


def test_corporate_registration_numbers_expose_their_corporate_number():
    result = validate_registration_number("T1010001153225")
    assert result.valid
    assert result.corporate_number == "1010001153225"


def test_separators_are_stripped():
    assert validate_corporate_number("1010-0011-53225").valid
    assert validate_registration_number("T1010-001153225").valid


@pytest.mark.parametrize("bad", ["", "123", "abcdefghijklm", "12345678901234"])
def test_malformed_input_is_rejected(bad):
    assert not validate_corporate_number(bad).valid


def test_is_valid_routes_by_prefix():
    assert is_valid("T1010001153225")
    assert is_valid("1010001153225")
    assert not is_valid("2010001153225")
    assert not is_valid("nonsense")
