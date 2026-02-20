import logging
from typing import Union

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(filename="./logs/masks.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(number: Union[str, int]) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску.
    Видны первые 6 цифр и последние 4 цифры, остальные символы
    отображаются звездочками, номер разбит по блокам по 4 цифры, разделенным пробелами."""
    logger.info("Начало маскирования номера карты")
    new_number = str(number)
    if len(new_number) != 16:
        logger.error(f"Ошибка: Неверная длина номера карты ({len(new_number)})")
        raise ValueError("Номер карты должен содержать 16 цифр")

    mask_number = new_number[:6] + "******" + new_number[12:]
    formatted_mask = " ".join([mask_number[i : i + 4] for i in range(0, len(mask_number), 4)])
    logger.info("Номер карты успешно замаскирован")
    return formatted_mask


def get_mask_account(number: Union[str, int]) -> str:
    """Функция принимает на вход номер счета и возвращает его маску.
    Видны только последние 4 цифры номера, а перед ними — две звездочки."""
    new_number = str(number)
    if len(new_number) < 4:
        logger.warning("Номер счета слишком короткий для стандартного маскирования")
    masked_account = "**" + new_number[-4:]
    logger.info("Номер счета успешно замаскирован")
    return masked_account
