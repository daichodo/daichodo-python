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


def test_sole_traders_are_valid_without_a_corporate_number():
    # Roughly half the register. Rejecting them would reject half of everything.
    result = validate_registration_number("T1234567890123")
    assert result.valid
    assert result.corporate_number is None
    assert "法人番号" in result.reason


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
