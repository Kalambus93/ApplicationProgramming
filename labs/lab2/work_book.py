import requests as rq
from bs4 import BeautifulSoup
import re
import os
import csv


def download_dirty_html(path_site: list[str]) -> list[str]:

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
    i = 1
    for book in books:
        url = "https://books.toscrape.com/" + book["cover_src"].replace("../", "")
        img = rq.get(url, timeout=10)

        path = f"{folder}/covers/{i}_{book['name']}.jpg"
        with open(path, "wb") as f:
            f.write(img.content)

        i += 1


def annotation_csv(path_annotation: str, expensive_books: list[dict]) -> None:
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
