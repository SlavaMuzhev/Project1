import json
import os
from typing import Any, List


def get_transactions_data(path: Any) -> List[Any]:
    """
    Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях
    """
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        return []

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []
