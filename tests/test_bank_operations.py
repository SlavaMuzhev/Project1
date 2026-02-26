import pytest
from src.bank_operations import process_bank_search, process_bank_operations
from tests.conftest import transactions


def test_process_bank_search_found(transactions:list)->list:
    """Тест успешного поиска строки"""
    result = process_bank_search(transactions, "Перевод организации")
    assert len(result) == 2
    assert result[0]["id"] == 939719570
    assert result[1]["id"] == 594226727


def test_process_bank_search_no_match(transactions:list)->list:
    """Тест когда совпадений нет"""
    result = process_bank_search(transactions, "Снятие наличных")
    assert result == []


def test_process_bank_search_empty_data(no_transactions:list)->list:
    """Тест с пустым списком данных"""
    assert process_bank_search([], "перевод") == []


def test_process_bank_search_none_description(transaction_description_none):
    """Тест обработки None"""
    result = process_bank_search(transaction_description_none, "")
    assert result == []


def test_process_bank_search_non_string_description(transaction_no_description):
    """Тест обработки отсутствующих ключа"""
    result = process_bank_search(transaction_no_description, "")
    assert result == []


def test_process_bank_search_special_chars(transaction_description_with_spec):
    """Тест поиска строки со спецсимволами"""
    result = process_bank_search(transaction_description_with_spec, "(МСК) +")
    assert len(result) == 1
    assert result[0]["id"] == 939719570


def test_process_bank_operations_basic(transactions:list)->list:
    """Тест подсчета существующих категорий"""
    categories = ["Перевод организации", "Перевод с карты на карту"]
    result = process_bank_operations(transactions, categories)

    assert result == {
        "Перевод организации": 2,
        "Перевод с карты на карту": 1

    }


def test_process_bank_operations_with_missing_in_data(transactions:list)->list:
    """Тест когда категория указана, но её нет в данных"""
    categories = ["Снятие наличных", "Открытие вклада"]
    result = process_bank_operations(transactions, categories)

    assert result["Снятие наличных"] == 0
    assert result["Открытие вклада"] == 0


def test_process_bank_operations_empty_list():
    """Тест с пустым списком транзакций."""
    categories = ["Перевод организации"]
    result = process_bank_operations([], categories)

    assert result == {"Перевод организации": 0}


def test_process_bank_operations_no_categories(transactions:list)->list:
    """Тест когда список категорий пуст."""
    result = process_bank_operations(transactions, [])
    assert result == {}


def test_process_bank_operations_none_description(transaction_description_none):
    """Тест обработки None"""
    categories = [None]
    result = process_bank_operations(transaction_description_none, categories)
    assert result == {None: 1}


def test_process_bank_operations_non_description(transaction_no_description):
    """Тест обработки отсутствующих ключа"""
    result = process_bank_search(transaction_no_description, "")
    assert result == []




