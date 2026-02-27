import os
from pathlib import Path
from src.utils import get_transactions_data
from src.transaction_loader import reading_transactions_from_csv, reading_transactions_from_excel
from src.processing import filter_by_state, sort_by_date
from src.bank_operations import process_bank_search
from src.widget import get_date, mask_account_card
from src.generators import filter_by_currency


def main():
    """
    Функция отвечает за основную логику проекта и связывает функциональности между собой
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями")
    while True:
        print("Выберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")

        choice = input("Ваш выбор: ").strip()

        # Загрузка данных
        if choice == '1':
            print("\nДля обработки выбран JSON-файл")
            data = get_transactions_data(Path(os.path.join('data', 'operations.json')))
            break
        elif choice == '2':
            print("\nДля обработки выбран CSV-файл")
            data = reading_transactions_from_csv(Path(os.path.join('data', 'transactions.csv')))
            break
        elif choice == '3':
            print("\nДля обработки выбран XLSX-файл")
            data = reading_transactions_from_excel(Path(os.path.join('data', 'transactions_excel.xlsx')))
            break
        else:
            print("Ошибка: Неверный пункт меню")

    if not data:
        data = []
        print("Данные не загружены или файл пуст")

    # Фильтрация по статусу
    valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        status = input("\nВведите статус, по которому необходимо выполнить фильтрацию.\n"
                       "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n\n"
                       "Ваш выбор: ").upper().strip()

        if status in valid_statuses:
            data = filter_by_state(data, status)
            print(f"Операции отфильтрованы по статусу \"{status}\"")
            break
        else:
            print(f"Статус операции \"{status}\" недоступен")

    # Сортировка по дате
    while True:
        is_sort = input("\nОтсортировать операции по дате? Да/Нет\nВаш выбор: ").lower()
        if is_sort in ['да', 'нет']:
            break
        print("Пожалуйста, ответьте 'Да' или 'Нет'")
    if is_sort == "да":
        while True:
            order = input("Отсортировать по возрастанию или по убыванию?\nВаш выбор: ").lower()
            if "возраст" in order:
                data = sort_by_date(data, False)
                break
            elif "убыв" in order:
                data = sort_by_date(data, True)
                break
            else:
                print("Введите 'по возрастанию' или 'по убыванию'")

    # Фильтрация по валюте
    while True:
        is_rub = input("\nВыводить только рублевые транзакции? Да/Нет\nВаш выбор: ").lower()
        if is_rub in ['да', 'нет']:
            break
        print("Пожалуйста, введите 'Да' или 'Нет'")

    if is_rub == "да":
        data = list(filter_by_currency(data, "RUB"))

    # Фильтрация по слову в описании
    while True:
        is_search = input(
            "\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет\nВаш выбор: ").lower()
        if is_search in ['да', 'нет']:
            break
        print("Пожалуйста, введите 'Да' или 'Нет'")
    if is_search == "да":
        while True:
            search_query = input("Введите строку для поиска\nВаш выбор: ")
            if search_query:
                data = process_bank_search(data, search_query)
                break
            print("Строка поиска не может быть пустой")

    # Итоговый вывод
    print("\nРаспечатываю итоговый список транзакций...\n")

    if not data:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
    else:
        print(f"Всего банковских операций в выборке: {len(data)}\n")
        for transaction in data:
            date = get_date(transaction.get("date"))
            description = transaction.get('description', 'Нет описания транзакции')
            from_val = transaction.get('from')
            to_val = transaction.get('to')
            from_info = str(from_val) if (from_val and str(from_val).lower() != 'nan') else ""
            to_info = str(to_val) if (to_val and str(to_val).lower() != 'nan') else ""
            try:
                if from_info:
                    mask_from_info = mask_account_card(from_info)
                else:
                    mask_from_info = ""
                mask_to_info = mask_account_card(to_info) if to_info else "Неизвестный счет"
                if mask_from_info:
                    route = f"{mask_from_info} -> {mask_to_info}"
                else:
                    route = mask_to_info

            except ValueError:
                route = f"{from_info} -> {to_info}"

            amount = transaction.get('operationAmount', {}).get('amount')
            if amount is None:
                amount = transaction.get('amount')
            currency = transaction.get('operationAmount', {}).get('currency', {}).get('name')
            if currency is None:
                currency = transaction.get('currency_name')


            print(f"{date} {description}")
            print(f"{route}")
            print(f"Сумма: {amount} {currency}\n")

if __name__ == "__main__":
    main()