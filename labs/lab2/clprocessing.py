import argparse


def processing_command() -> tuple[int, str, str]:
    """
    Читает аргументы командной строки
    :return: кортеж аргументов командной строки
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("number_book", type=int, help="Enter number of books")
    parser.add_argument(
        "save_result_dir", type=str, help="Enter path for recording result"
    )
    parser.add_argument("annotation", type=str, help="Enter path annotation")

    args = parser.parse_args()

    return args.number_book, args.save_result_dir, args.annotation
