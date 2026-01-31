from typing import Any, Dict, Generator, Iterator, List


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]:
    """Функция принимает на вход список словарей, представляющих транзакции.
    Функция возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной"""
    for transaction in transactions:
        amount = transaction.get("operationAmount") or {}
        currency_data = amount.get("currency") or {}
        currency_code = currency_data.get("code", "Error")
        if currency_code == "Error":
            raise ValueError("В транзакции не указан код валюты")
        elif currency_code == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[Dict[str, Any]]:
    """Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        transaction_description = transaction.get("description", "Error")
        if transaction_description == "Error":
            raise ValueError("Нет описания транзакции")
        else:
            yield transaction_description


def card_number_generator(start: int = 1, end: int = 9999999999999999) -> Generator[str, None, None]:
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    for i in range(start, end + 1):
        number_str = f"{i:016d}"
        yield f"{number_str[:4]} {number_str[4:8]} {number_str[8:12]} {number_str[12:]}"
