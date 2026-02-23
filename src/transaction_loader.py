import csv
from pathlib import Path
from typing import Any, Dict, List, cast

import pandas as pd


def reading_transactions_from_csv(file_path: Path) -> List[Dict[str, Any]]:
    """Функция для считывания финансовых операций из CSV. Выдает список словарей с транзакциями"""
    with open(file_path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def reading_transactions_from_excel(file_path: Path) -> List[Dict[str, Any]]:
    """Функция для считывания финансовых операций из Excel. Выдает список словарей с транзакциями"""
    excel_data = pd.read_excel(file_path)
    return cast(List[Dict[str, Any]], excel_data.to_dict(orient="records"))
