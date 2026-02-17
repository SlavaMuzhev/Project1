import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')


def get_transaction_amount(transaction):
    """
    Принимает транзакцию и возвращает сумму в рублях.
    Если валюта USD/EUR, выполняет конвертацию через API.
    """
    op_amount = transaction.get('operationAmount', {})
    amount = float(op_amount.get('amount', 0))
    currency = op_amount.get('currency', {}).get('code')

    if currency == 'RUB':
        return amount

    if currency in ['USD', 'EUR']:
        try:
            url = f"https://api.apilayer.com{currency}&amount={amount}"
            response = requests.get(url, headers={"apikey": API_KEY}, timeout=10)
            response.raise_for_status()
            return float(response.json().get('result', 0.0))
        except Exception as e:
            print(f"Ошибка API: {e}")
            return 0.0

    return 0.0


