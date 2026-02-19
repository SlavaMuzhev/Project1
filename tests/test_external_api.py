import unittest
from unittest.mock import Mock, patch

from src.external_api import get_transaction_amount


class TestTransactionAmount(unittest.TestCase):

    @patch("src.external_api.requests.get")
    def test_get_transaction_amount_usd(self, mock_get: Mock) -> None:
        """Тест конвертации из USD (успешный запрос)."""
        # Настраиваем Mock для имитации ответа API
        mock_response = Mock()
        mock_response.ok = True
        mock_response.json.return_value = {"result": 7500.0}
        mock_get.return_value = mock_response

        transaction = {"operationAmount": {"amount": "100.00", "currency": {"code": "USD"}}}

        result = get_transaction_amount(transaction)

        self.assertEqual(result, 7500.0)
        mock_get.assert_called_once()

    def test_get_transaction_amount_rub(self) -> None:
        """Тест транзакции в RUB (без вызова API)."""
        transaction = {"operationAmount": {"amount": "500.50", "currency": {"code": "RUB"}}}
        result = get_transaction_amount(transaction)
        self.assertEqual(result, 500.50)

    @patch("src.external_api.requests.get")
    def test_get_transaction_amount_api_error(self, mock_get: Mock) -> None:
        """Тест поведения при ошибке API (возврат 0.0)."""
        # Имитируем ошибку (например, 404 или таймаут)
        mock_get.side_effect = Exception("API Connection Error")

        transaction = {"operationAmount": {"amount": "10.00", "currency": {"code": "EUR"}}}

        result = get_transaction_amount(transaction)
        self.assertEqual(result, 0.0)

    def test_get_transaction_amount_empty(self) -> None:
        """Тест обработки пустой транзакции."""
        result = get_transaction_amount({})
        self.assertEqual(result, 0.0)
