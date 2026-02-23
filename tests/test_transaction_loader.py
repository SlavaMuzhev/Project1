from pathlib import Path

import pytest

from src.transaction_loader import reading_transactions_from_csv, reading_transactions_from_excel


def test_reading_transactions_from_csv(temp_csv: Path) -> None:
    result = reading_transactions_from_csv(temp_csv)

    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["amount"] == "100"
    assert result[1]["currency"] == "USD"


def test_reading_transactions_from_excel(temp_excel: Path) -> None:
    result = reading_transactions_from_excel(temp_excel)

    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["amount"] == 100
    assert result[1]["id"] == 2


def test_csv_file_not_found() -> None:
    with pytest.raises(FileNotFoundError):
        reading_transactions_from_csv(Path("non_existent.csv"))
