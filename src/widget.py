from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_details_or_account: str) -> str:
    """Функция принимает один аргумент — строку, содержащую тип и номер карты или счета.
    Возвращает строку с замаскированным номером."""
    number = "".join(filter(lambda x: x.isdigit(), card_details_or_account))
    card_type_or_account = "".join(filter(lambda c: not c.isdigit(), card_details_or_account)).strip()
    if "Счет" in card_type_or_account:
        mask = get_mask_account(number)
    else:
        mask = get_mask_card_number(number)
    return f"{card_type_or_account} {mask}"


def get_date(data: str) -> str:
    """функцию, которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате ДД.ММ.ГГГГ."""
    return f"{data[8:10]}.{data[5:7]}.{data[:4]}"
