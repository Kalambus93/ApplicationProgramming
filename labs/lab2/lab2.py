import csv
import requests
from bs4 import BeautifulSoup

import work_book as wb
import clprocessing as cls


def main() -> None:
    # 0. Аргументы
    args = cls.processing_command()
    number_books = args[0]
    result_dir = args[1]
    annotation = args[2]

    # 1. Скачивание обложек
    list_paths_sites = []
    path_site = "https://books.toscrape.com/catalogue/page-"
    for i in range(1, 3):
        temp_site = path_site + str(i) + ".html"
        list_paths_sites.append(temp_site)

    # 1.1 Грязное скачивание текста
    dirty_html = wb.download_dirty_html(list_paths_sites)

    # 1.2 Преобразование в норм текст
    clean_html = wb.download_clean_html(dirty_html)

    # 1.3 Нахождение самых дорогих обложек
    top_expensive_number_books = sorted(
        clean_html, key=lambda b: b["price"], reverse=True
    )[:number_books]

    print(top_expensive_number_books)

    # 1.4 Скачивание самых дорогих обложек
    wb.download_expensive_books(top_expensive_number_books, result_dir)

    # 2. Аннотация
    wb.annotation_csv(annotation, top_expensive_number_books)


if __name__ == "__main__":
    main()
