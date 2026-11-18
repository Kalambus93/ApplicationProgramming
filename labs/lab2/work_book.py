import requests as rq
from bs4 import BeautifulSoup
import re
import os
import csv


def download_dirty_html(path_site: list[str]) -> list[str]:
    """
    Функция, которая считывает html код страниц
    :param path_site: путь сайта
    :return: грязный html страницы
    """

    pages = []

    for i in path_site:
        response = rq.get(i)
        html = response.text
        response.raise_for_status()
        response.encoding = "utf-8"
        pages.append(html)
        print(f"Просмотрена {i} страница")

    return pages


def download_clean_html(dirty_html: list[str]) -> list[dict]:
    """
    Функция, которая вытаскивает нужные теги (название книги, цена, путь к обложке)
    :param dirty_html: грязный html
    :return: список словарей {имя, цена, путь к обложке}
    """

    books: list[dict] = []

    for page_html in dirty_html:
        soup = BeautifulSoup(page_html, "html.parser")

        for card in soup.find_all("article", class_="product_pod"):
            name = card.find("h3").find("a")["title"]
            price_text = card.find("p", class_="price_color").get_text(strip=True)
            price = float(re.sub(r"[^\d.]", "", price_text))
            cover_src = card.find("img")["src"]

            books.append({"name": name, "price": price, "cover_src": cover_src})

    return books


def download_expensive_books(books: list[dict], folder: str) -> None:
    """
    Функция, которая скачивает самые дорогие обложки
    :param books: сортированный список словарей {имя, цена, путь к обложке}
    :param folder: папка, куда сохранять обложки
    """

    if os.path.exists(f"{folder}/covers"):
        for name in os.listdir(f"{folder}/covers"):
            os.remove(os.path.join(f"{folder}/covers", name))
        os.rmdir(f"{folder}/covers")

    os.mkdir(f"{folder}/covers")

    i = 1
    for book in books:
        url = "https://books.toscrape.com/" + book["cover_src"].replace("../", "")
        img = rq.get(url, timeout=10)

        path = f"{folder}/covers/{i}_{book['name']}.jpg"
        with open(path, "wb") as f:
            f.write(img.content)

        print(f"Скачана обложка №{i}")
        i += 1


def annotation_csv(path_annotation: str, expensive_books: list[dict]) -> None:
    """
    Функция, которая скачивает самые дорогие обложки
    :param path_annotation: путь аннотации
    :param expensive_books: сортированный список словарей {имя, цена, путь к обложке}
    """

    abs_pathes = []
    rel_pathes = []

    for book in expensive_books:
        rel_path = os.path.relpath(f"../data/lab2/covers/{book["name"]}")
        abs_path = os.path.abspath(f"../data/lab2/covers/{book["name"]}")
        rel_pathes.append(rel_path)
        abs_pathes.append(abs_path)

    with open(path_annotation, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["relative_path", "absolute_path"])

        for i in range(len(expensive_books)):
            writer.writerow([rel_pathes[i], abs_pathes[i]])


class PathIterator:
    def __init__(self, csv_file):
        with open(csv_file, newline="", encoding="utf-8") as f:
            self.rows = list(csv.DictReader(f))
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= len(self.rows):
            raise StopIteration
        row = self.rows[self.i]
        self.i += 1
        return row
