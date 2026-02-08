import functools
import time
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Декоратор для логирования времени работы, результата или ошибок функции.
    """

    def wrapper(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            time_1 = time.time()
            formatted_time_1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_1))
            try:
                result = func(*args, **kwargs)
                time_2 = time.time()
                formatted_time_2 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_2))
                log_message = (
                    f"{func.__name__} ok Результат: {result}\n"
                    f"Время начала: {formatted_time_1} Время завершения: {formatted_time_2}\n"
                    f"Время работы: {time_2 - time_1:.7f}\n"
                )
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_message)
                else:
                    print(log_message)
                return result
            except Exception as e:
                time_err = time.time()
                formatted_time_err = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_err))
                log_message = (
                    f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n"
                    f"Время начала: {formatted_time_1} Время завершения: {formatted_time_err}\n"
                    f"Время работы: {time_err - time_1:.7f}\n"
                )
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_message)
                else:
                    print(log_message)

        return inner

    return wrapper
