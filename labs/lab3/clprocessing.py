import argparse


def processing_command() -> tuple[str, str]:
    """
    Читает аргументы командной строки
    :return: кортеж аргументов командной строки
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("original_file", type=str, help="Enter original file")
    parser.add_argument("result", type=str, help="Enter path for recording result")

    args = parser.parse_args()

    return args.original_file, args.result
