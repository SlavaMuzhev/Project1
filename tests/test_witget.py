import pytest

from src.widget import mask_account_card, get_date



def test_mask_account_card(account_details):
    assert mask_account_card(account_details) == "Счет **4305"


@pytest.mark.parametrize(
    "data, expected", [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 7777002289600943", "Maestro 7777 00** **** 0943")
    ]
)
def test_mask_account_card(data, expected):
    assert mask_account_card(data) == expected


def test_mask_account_card_fail():
    with pytest.raises(ValueError, match="Номер карты должен содержать 16 цифр"):
        mask_account_card("123412341234")


def test_get_date(data):
    assert get_date(data) == "11.03.2024"






