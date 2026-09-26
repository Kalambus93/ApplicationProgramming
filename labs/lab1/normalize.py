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


def normalize_gender(genders: list[str]) -> list[str]:

    """
    Нормализует значения пола.
    :param genders: список строк с исходными значениями пола.
    :return: список строк, где значения приведены к "Мужской" или "Женский".
    """

    temp_list = []
    for i in range(len(genders)):
        temp_list.append("Мужской") if genders[i] == 'м' or genders[i] == 'М' or genders[i] == 'Мужской' or genders[i] == 'мужской' else temp_list.append("Женский")
    return temp_list


def normalize_data_connection(data_connections: list[str]) -> list[str]:

    """
    Нормализует контактные данные (email или номер телефона).
    :param data_connections: список строк с исходными контактами.
    :return: список строк с валидными email, телефонами в формате +7... или "-", если данные некорректны.
    """

    pattern_email = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,4}"
    pattern_phone_clean = r"^7\d{10}$"
    
    temp_list = []

    for item in data_connections:
        
        if re.fullmatch(pattern_email, item):
            temp_list.append(item)
            
        else:
            digits = re.sub(r'\D', '', item)

            digits = '7' + digits[1:]

            if re.fullmatch(pattern_phone_clean, digits):
                temp_list.append('+' + digits)
            else:
                temp_list.append('-')
    
    return temp_list