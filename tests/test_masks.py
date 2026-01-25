from typing import Union

import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(card_number: Union[str]) -> None:
    assert get_mask_card_number(card_number) == "1234 12** **** 1234"


@pytest.mark.parametrize("data, expected", [("12341234123412341234", "**1234"), ("774521", "**4521")])
def test_get_mask_account(data: str, expected: str) -> None:
    assert get_mask_account(data) == expected


def test_get_mask_card_number_fail() -> None:
    with pytest.raises(ValueError, match="Номер карты должен содержать 16 цифр"):
        get_mask_card_number("456789")
