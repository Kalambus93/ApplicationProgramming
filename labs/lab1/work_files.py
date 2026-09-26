import argparse


def enter_filename() -> str:

    """
    Получает имя файла из аргументов командной строки.
    :return: имя файла в виде строки.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type = str, help = 'Enter filename')
    args = parser.parse_args()
    return args.filename