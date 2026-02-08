import os
from typing import Any
from unittest.mock import mock_open, patch

from src.decorators import log


def test_log(capsys: Any) -> None:
    """Тест проверяет вывод в консоль"""
    t1, t2 = 1700000000.0, 1700000010.0
    fmt1, fmt2 = "2026-02-08 12:15:20", "2026-02-08 12:15:30"
    with (
        patch("src.decorators.time.time") as m_time,
        patch("src.decorators.time.strftime") as m_strftime,
        patch("src.decorators.time.localtime"),
    ):

        m_time.side_effect = [t1, t2]
        m_strftime.side_effect = [fmt1, fmt2]

        @log()
        def my_function(x: int, y: int) -> int:
            return x + y

        result = my_function(1, 2)
        captured = capsys.readouterr().out
        assert result == 3
        assert "my_function ok" in captured
        assert "Результат: 3" in captured
        assert f"Время начала: {fmt1}" in captured
        assert f"Время завершения: {fmt2}" in captured
        assert "Время работы: 10.0" in captured


def test_log_file() -> None:
    """Тест проверяет запись в файл"""
    t1, t2 = 1700000000.0, 1700000010.0
    fmt1, fmt2 = "2026-02-08 12:15:20", "2026-02-08 12:15:30"
    filename = "mylog.txt"
    m_open = mock_open()
    with (
        patch("src.decorators.time.time") as m_time,
        patch("src.decorators.time.strftime") as m_strftime,
        patch("src.decorators.time.localtime"),
        patch("builtins.open", m_open),
    ):

        m_time.side_effect = [t1, t2]
        m_strftime.side_effect = [fmt1, fmt2]

        @log(filename=filename)
        def my_function(x: int, y: int) -> int:
            return x + y

        result = my_function(1, 2)

        m_open.assert_called_once_with(filename, "a", encoding="utf-8")
        handle = m_open()
        written_data = "".join(call.args[0] for call in handle.write.call_args_list)
        assert "my_function ok" in written_data
        assert f"Результат: {result}" in written_data
        assert f"Время начала: {fmt1}" in written_data
        assert f"Время завершения: {fmt2}" in written_data
        assert "Время работы: 10.0" in written_data


def test_log_error_file() -> None:
    """Тест проверяет запись ошибки в файл"""

    @log(filename="mylog.txt")
    def divide(a: int, b: int) -> float:
        return a / b

    result = divide(1, 0)
    assert result is None

    assert os.path.exists("mylog.txt")

    with open("mylog.txt", "r", encoding="utf-8") as f:
        content = f.read()
    assert "divide error: ZeroDivisionError" in content
    assert "Inputs: (1, 0)" in content


def test_log_error_console(capsys: Any) -> None:
    """Тест проверяет вывод ошибки в консоль"""
    t1, t2 = 1700000000.0, 1700000001.0
    fmt_time = "2026-02-08 15:40:00"

    # Патчим время (укажите правильный путь к вашему модулю!)
    with (
        patch("src.decorators.time.time") as m_time,
        patch("src.decorators.time.strftime") as m_strftime,
        patch("src.decorators.time.localtime"),
    ):

        m_time.side_effect = [t1, t2]
        m_strftime.return_value = fmt_time

        @log()
        def divide(a: int, b: int) -> float:
            return a / b

        divide(1, 0)

    captured = capsys.readouterr().out

    assert "divide error: ZeroDivisionError" in captured
    assert "Inputs: (1, 0), {}" in captured
    assert f"Время начала: {fmt_time}" in captured
    assert "Время работы: 1.0" in captured
