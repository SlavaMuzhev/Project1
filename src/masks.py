from typing import Union


def get_mask_card_number(number: Union[str, int]) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску.
    Dидны первые 6 цифр и последние 4 цифры, остальные символы
    отображаются вездочками, номер разбит по блокам по 4 цифры,разделенным пробелами."""
    new_number = str(number)
    mask_number = new_number[:6] + "******" + new_number[12:]
    return " ".join([mask_number[i : i + 4] for i in range(0, len(mask_number), 4)])


def get_mask_account(number: Union[str, int]) -> str:
    """Функция принимает на вход номер счета и возвращает его маску.
    видны только последние 4 цифры номера, а перед ними — две звездочки."""
    new_number = str(number)
    return "**" + new_number[-4:]
