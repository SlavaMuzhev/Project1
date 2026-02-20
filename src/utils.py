import json
import logging
import os
from typing import Any, List

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(filename="./logs/utils.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transactions_data(path: Any) -> List[Any]:
    """
    Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях
    """
    logger.info(f"Попытка чтения данных из файла: {path}")
    if not os.path.exists(path):
        logger.error(f"Файл не найден по пути: {path}")
        return []

    if os.path.getsize(path) == 0:
        logger.warning(f"Файл пуст: {path}")
        return []

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            logger.error(f"Ошибка структуры: ожидался список, получен {type(data)} в {path}")
            return []

        logger.info(f"Успешно загружено транзакций: {len(data)}")
        return data

    except json.JSONDecodeError as e:
        logger.error(f"Ошибка декодирования JSON в файле {path}: {e}")
        return []
    except Exception as e:
        logger.error(f"Непредвиденная ошибка при чтении {path}: {e}")
        return []
