import functools
import time


def log(filename=None):
    """
    Декоратор для логирования времени работы, результата или ошибок функции.
    """
    def wrapper(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            try:
                time_1 = time.time()
                formatted_time_1 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time_1))
                result = func(*args, **kwargs)
                time_2 = time.time()
                formatted_time_2 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time_2))
                log_message = f"""
                {func.__name__} ok Результат: {result} 
                Время начала: {formatted_time_1} Время завершения: {formatted_time_2}
                Время работы: {time_2-time_1}
                """
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_message)
                else:
                    print(log_message)
                return result
            except Exception as e:
                log_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_message)
        return inner
    return wrapper


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)