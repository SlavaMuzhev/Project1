import pytest

@pytest.fixture
def card_number():
    return "1234123412341234"


@pytest.fixture
def account_number():
    return "12341234123412341234"


@pytest.fixture
def account_details():
    return "Счет 73654108430135874305"


@pytest.fixture
def same_date():
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2019-07-03T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2019-07-03T08:21:33.419441'}
    ]


@pytest.fixture
def status_no_state():
    return [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]


