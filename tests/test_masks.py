import pytest

from src.masks import get_mask_card_number, get_mask_account



def test_get_mask_card_number(card_number):
    assert get_mask_card_number(card_number) == "1234 12** **** 1234"


@pytest.mark.parametrize("data, expected", [("12341234123412341234", "**1234"), ("774521", "**4521")])
def test_get_mask_account(data, expected):
    assert get_mask_account(data) == expected


def test_get_mask_card_number_fail():
    with pytest.raises(ValueError, match="Номер карты должен содержать 16 цифр"):
        get_mask_card_number("456789")

