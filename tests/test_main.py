from unittest.mock import MagicMock, patch

from main import main


@patch("main.get_transactions_data")
@patch("builtins.input")
@patch("builtins.print")
def test_main_full_flow(
    mock_print: MagicMock, mock_input: MagicMock, mock_json: MagicMock, transactions_for_main: list
) -> None:
    """
    Тест полного цикла программы:
    Выбор JSON -> Статус EXECUTED -> Без сортировки -> Без фильтра валют -> Без поиска по слову.
    """
    mock_json.return_value = transactions_for_main

    mock_input.side_effect = ["1", "EXECUTED", "нет", "нет", "нет"]

    main()

    printed_output = "".join([str(call.args) for call in mock_print.call_args_list])

    assert "Всего банковских операций в выборке: 1" in printed_output
    assert "Перевод со счета на счет" in printed_output
    assert "Счет **4719 -> Счет **1160" in printed_output
    assert "Сумма: 43318.34 руб." in printed_output


@patch("main.get_transactions_data")
@patch("builtins.input")
@patch("builtins.print")
def test_main_filter_by_word(
    mock_print: MagicMock, mock_input: MagicMock, mock_json: MagicMock, transactions_for_main: list
) -> None:
    """Тест поиска по слову, которое есть в описании (со счета на счет)"""
    mock_json.return_value = transactions_for_main

    mock_input.side_effect = ["1", "EXECUTED", "нет", "нет", "да", "счета"]

    main()

    printed_output = "".join([str(call.args) for call in mock_print.call_args_list])
    assert "Всего банковских операций в выборке: 1" in printed_output
    assert "Перевод со счета на счет" in printed_output


@patch("main.get_transactions_data")
@patch("builtins.input")
@patch("builtins.print")
def test_main_filter_by_word_not_found(
    mock_print: MagicMock, mock_input: MagicMock, mock_json: MagicMock, transactions_for_main: list
) -> None:
    """Тест поиска по слову, которого нет в описании"""
    mock_json.return_value = transactions_for_main

    mock_input.side_effect = ["1", "EXECUTED", "нет", "нет", "да", "Криптовалюта"]

    main()

    printed_output = "".join([str(call.args) for call in mock_print.call_args_list])
    assert "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации" in printed_output


@patch("main.get_transactions_data")
@patch("builtins.input")
@patch("builtins.print")
def test_main_sorting_ascending(
    mock_print: MagicMock, mock_input: MagicMock, mock_json: MagicMock, transactions_for_main: list
) -> None:
    """Тест выбора сортировки по возрастанию"""
    mock_json.return_value = transactions_for_main

    mock_input.side_effect = ["1", "EXECUTED", "да", "по возрастанию", "нет", "нет"]

    main()

    printed_output = "".join([str(call.args) for call in mock_print.call_args_list])

    assert "Распечатываю итоговый список транзакций" in printed_output
