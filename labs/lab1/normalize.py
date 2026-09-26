import re


def normalize_text(text: list[str]) -> None:

    """
    Приводит первую букву каждого элемента списка к заглавной.
    :param text: список строк для нормализации.
    :return: None
    """

    for i in range(len(text)):
        text[i] = text[i].title()

def normalize_date(dates: list[str]) -> list[str]:

    """
    Нормализует даты, проверяя их на корректность.
    :param dates: список кортежей строк вида (день, месяц, год).
    :return: список строк с датами в формате ДД.ММ.ГГГГ или "-.-.-" для некорректных дат.
    """

    temp_list = []
    
    for i in range(len(dates)):
        if 1 <= int(dates[i][0]) <= 31 and 1 <= int(dates[i][1]) <= 12 and 1900 <= int(dates[i][2]) <= 2026:
            temp_list.append(dates[i][0] + '.' + dates[i][1] + '.' + dates[i][2])
        else:
            temp_list.append("-.-.-")

    return temp_list 