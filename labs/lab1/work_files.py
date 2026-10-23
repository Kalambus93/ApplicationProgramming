import argparse


def enter_filename() -> list[str]:

    """
    Получает имя файла из аргументов командной строки.
    :return: имя файла в виде строки.
    """

    list = []

    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type = str, help = 'Enter filename')
    parser.add_argument('write_filename', type = str, help = 'Enter filename for write result')
    args = parser.parse_args()

    list.append(args.filename)
    list.append(args.write_filename)

    return list

def open_file(filename: str) -> str:

    """
    Открывает файл и считывает его содержимое.
    :param filename: имя файла для чтения.
    :return: содержимое файла в виде строки.
    """

    text = ""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
    except FileNotFoundError as exc:
        print(f"Error:{exc}")

    return text


def open_file_w(normalize_data_bases: list[list[str]], file_path: str = "result.txt") -> None:

    """
    Записывает нормализованные данные в текстовый файл.
    :param normalize_data_bases: список списков строк, содержащий нормализованные данные (фамилии, имена и т.д.).
    :return: None
    """

    try:
        with open(file_path, "w", encoding="utf-8") as file:
            for i in range(len(normalize_data_bases[0])):
                file.write(f"{i+1})\n")
                file.write(f"Фамилия: {normalize_data_bases[0][i]}\n")
                file.write(f"Имя: {normalize_data_bases[1][i]}\n")
                file.write(f"Пол: {normalize_data_bases[2][i]}\n")
                file.write(f"Дата рождения: {normalize_data_bases[3][i]}\n")
                file.write(f"Номер телефона или email: {normalize_data_bases[4][i]}\n")
                file.write(f"Город: {normalize_data_bases[5][i]}\n")
                file.write(f"\n")

    except OSError as exc:
        print(f"Ошибка при записи в файл: {exc}")