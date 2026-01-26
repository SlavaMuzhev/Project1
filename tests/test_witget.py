from typing import Union

import pytest

from src.widget import get_date, mask_account_card


def test_mask_account(account_details: str) -> None:
    assert mask_account_card(account_details) == "Счет **4305"


@pytest.mark.parametrize(
    "data, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 7777002289600943", "Maestro 7777 00** **** 0943"),
    ],
)
def test_mask_account_card(data: Union[str], expected: str) -> None:
    assert mask_account_card(data) == expected


def test_mask_account_card_fail() -> None:
    with pytest.raises(ValueError, match="Номер карты должен содержать 16 цифр"):
        mask_account_card("123412341234")


def test_get_date(data: Union[str]) -> None:
    assert get_date(data) == "11.03.2024"
