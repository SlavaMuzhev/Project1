from typing import Any, Dict, List


def filter_by_state(list_of_dicts: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция принимает список словарей и опционально значение для ключа state.
    Возвращает новый список словарей, содержащий только те
    словари, у которых ключ state соответствует указанному значению"""
    filtered_list = [d for d in list_of_dicts if d.get("state") == state]
    return filtered_list


def sort_by_date(list_of_dicts: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """Функция принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание). Возвращает новый список отсортированный по дате (date)"""
    sorted_list = sorted(list_of_dicts, key=lambda item: item["date"], reverse=descending)
    return sorted_list
