import csv
import requests
from bs4 import BeautifulSoup

import work_book as wb


def main() -> None:
    # 1. Скачивание обложек
    list_paths_sites = []
    path_site = "https://books.toscrape.com/catalogue/page-"
    for i in range(1, 51):
        temp_site = path_site + str(i) + ".html"
        list_paths_sites.append(temp_site)

    # 1.1 Грязное скачивание текста
    # dirty_html = wb.download_dirty_html(path_site)
    # 1.2 Преобразование в норм текст


if __name__ == "__main__":
    main()
