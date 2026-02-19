from src.utils import get_transactions_data


def test_get_transactions_valid(temp_json_file):
    """Проверка работы с корректным списком транзакций"""
    data = [{"id": 1, "amount": "100.0"}, {"id": 2, "amount": "200.0"}]
    path = temp_json_file(data)
    assert get_transactions_data(path) == data

def test_get_transactions_empty_list(temp_json_file):
    """Проверка работы с пустым списком в JSON"""
    path = temp_json_file([])
    assert get_transactions_data(path) == []

def test_get_transactions_not_a_list(temp_json_file):
    """Проверка: если в JSON объект (словарь) вместо списка"""
    path = temp_json_file({"id": 1})
    assert get_transactions_data(path) == []

def test_get_transactions_file_not_found():
    """Проверка: файл не существует"""
    assert get_transactions_data("non_existent_file.json") == []

def test_get_transactions_empty_file(temp_json_file):
    """Проверка: файл полностью пуст"""
    path = temp_json_file("")
    assert get_transactions_data(path) == []

def test_get_transactions_invalid_json(temp_json_file):
    """Проверка: файл содержит некорректный JSON"""
    path = temp_json_file("{ 'invalid': json }")
    assert get_transactions_data(path) == []