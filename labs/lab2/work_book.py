import requests as rq
from bs4 import BeautifulSoup
import re


def download_dirty_html(path_site: list[str]) -> list[str]:

    pages = []

    for i in path_site:
        response = rq.get(i)
        html = response.text
        pages.append(html)
        print(f"Просмотрена {i} страница")

    return pages


def download_clean_html(dirty_html: list[str]) -> list[dict]:
    books: list[dict] = []

    for page_html in dirty_html:
        soup = BeautifulSoup(page_html, "html.parser")

        for card in soup.select("article.product_pod"):
            name = card.select_one("h3 a")["title"]
            price_text = card.select_one("p.price_color").get_text(strip=True)
            price = float(re.sub(r"[^\d.]", "", price_text))

            books.append({"name": name, "price": price})

    return books
