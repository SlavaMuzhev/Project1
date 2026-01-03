from typing import List, Dict, Any


def filter_by_state(list_of_dicts: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """ Функция принимает список словарей и опционально значение для ключа state.
    Возвращает новый список словарей, содержащий только те
    словари, у которых ключ state соответствует указанному значению """
    filtered_list = [d for d in list_of_dicts if d.get('state') == state]
    return filtered_list
