import re
from collections import Counter


def process_bank_search(data:list[dict], search:str)->list[dict]:
    """
    Функция принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка.
    """
    filtered_list = []
    pattern = re.compile(re.escape(search), re.IGNORECASE)

    for transaction in data:
        description = transaction.get("description")

        if isinstance(description, str):
            if pattern.search(description):
                filtered_list.append(transaction)

    return filtered_list


def process_bank_operations(data:list[dict], categories:list)->dict:
    """
    Функцию принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории.
    """
    descriptions = [
        transaction.get('description')
        for transaction in data
        if transaction.get('description') in categories
    ]

    counts = Counter(descriptions)

    return {category: counts.get(category, 0) for category in categories}
