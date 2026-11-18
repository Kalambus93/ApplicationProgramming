import csv
import requests
from bs4 import BeautifulSoup

import work_book as wb
import clprocessing as cls


def main() -> None:
    """
    Основная функция
    """
    args = cls.processing_command()
    number_books = args[0]
    result_dir = args[1]
    annotation = args[2]

    list_paths_sites = []
    path_site = "https://books.toscrape.com/catalogue/page-"
    for i in range(1, 51):
        temp_site = path_site + str(i) + ".html"
        list_paths_sites.append(temp_site)

    dirty_html = wb.download_dirty_html(list_paths_sites)
    clean_html = wb.download_clean_html(dirty_html)

    top_expensive_number_books = sorted(
        clean_html, key=lambda b: b["price"], reverse=True
    )[:number_books]

    print(f"Самые дорогие {number_books} книг")
    for i in top_expensive_number_books:
        print(f"Название: {i["name"]}, Цена: {i["price"]}")

    wb.download_expensive_books(top_expensive_number_books, result_dir)

    wb.annotation_csv(annotation, top_expensive_number_books)

    print("Проход итератором по путям")
    for path in wb.PathIterator(annotation):
        print(path)


if __name__ == "__main__":
    main()
