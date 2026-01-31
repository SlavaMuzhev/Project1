import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_usd(transactions: list) -> None:
    """Тесты, проверяющие, что функция корректно фильтрует транзакции по заданной валюте."""
    usd_transactions = filter_by_currency(transactions, "USD")
    assert next(usd_transactions) == transactions[0]
    assert next(usd_transactions) == transactions[1]
    assert next(usd_transactions) == transactions[3]


def test_filter_by_currency_rub(transactions: list) -> None:
    rub_transactions = filter_by_currency(transactions, "RUB")
    assert next(rub_transactions) == transactions[2]
    assert next(rub_transactions) == transactions[4]


def test_filter_by_currency_no_match(transactions: list) -> None:
    """Проверка того, что генератор не завершается ошибкой при обработке списка
    без соответствующих валютных операций."""
    generator = filter_by_currency(transactions, "GBP")
    # Проверяем, что итератор пуст
    with pytest.raises(StopIteration):
        next(generator)


def test_filter_by_currency_no_transactions(no_transactions: list) -> None:
    """Проверка: генератор не падает и остается пустым, если на вход подается пустой список.."""
    generator = filter_by_currency(no_transactions, "USD")
    # Проверяем, что итератор пуст
    with pytest.raises(StopIteration):
        next(generator)


def test_filter_by_currency_missing_code(transaction_no_code: list) -> None:
    """Проверка: В транзакции не указан код валюты"""
    generator = filter_by_currency(transaction_no_code, "USD")
    with pytest.raises(ValueError, match="В транзакции не указан код валюты"):
        next(generator)


def test_transaction_descriptions(transactions: list) -> None:
    """Проверка: функция возвращает корректные описания для каждой транзакции."""
    generator = transaction_descriptions(transactions)
    assert next(generator) == transactions[0]["description"]
    assert next(generator) == transactions[1]["description"]
    assert next(generator) == transactions[2]["description"]


def test_transaction_descriptions_missing_description(transaction_no_description: list) -> None:
    """Проверка: В транзакции не указано описания для транзакции"""
    generator = transaction_descriptions(transaction_no_description)
    with pytest.raises(ValueError, match="Нет описания транзакции"):
        next(generator)


def test_transaction_descriptions_no_transactions(no_transactions: list) -> None:
    """Проверка: генератор не падает и остается пустым, если на вход подается пустой список."""
    generator = transaction_descriptions(no_transactions)
    with pytest.raises(StopIteration):
        next(generator)


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (9999999999999999, 9999999999999999, ["9999 9999 9999 9999"]),
        (7, 5, []),
    ],
)
def test_card_number_generator(start: int, end: int, expected: list) -> None:
    assert list(card_number_generator(start, end)) == expected
