import re


from normalize import normalize_date, normalize_gender, normalize_text, normalize_data_connection
from work_files import enter_filename, open_file, open_file_w


def main() -> None:

    """
    Основная функция программы.
    Считывает данные, нормализует их и выводит результат.
    """

    filename = enter_filename()

    try:
        text = open_file(filename)
    except FileNotFoundError as exc:
        print(f"Error:{exc}")

    patterns = {
        'name': r"Имя:\s*(\w+)",
        'surname': r"Фамилия:\s*(\w+)",
        'gender': r"Пол:\s*(\w+)",
        'date': r"Дата рождения:\s*(\d+).(\d+).(\d+)",
        'data_connection': r"Номер телефона или email:\s*(.*)",
        'city': r"Город:\s*(?:г\.\s*)?(.+)"
    }

    names = re.findall(patterns['name'], text)
    surnames = re.findall(patterns['surname'], text)
    genders = re.findall(patterns['gender'], text)
    dates = re.findall(patterns['date'], text)
    data_connections = re.findall(patterns['data_connection'], text)
    cities = re.findall(patterns['city'], text)

    normalize_text(names)
    normalize_text(surnames)
    dates = normalize_date(dates)
    genders = normalize_gender(genders)
    data_connections = normalize_data_connection(data_connections)

    normalize_data_bases = [surnames, names, genders, dates, data_connections, cities] 

    open_file_w(normalize_data_bases)


if __name__ == "__main__":
    main()
