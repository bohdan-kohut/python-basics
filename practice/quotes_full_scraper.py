import requests
from bs4 import BeautifulSoup
import json
import time
time.sleep(1)

data = []

base_url = "https://quotes.toscrape.com/page/{}/"

for page in range(1, 6):
    print(f"Парсинг сторінки {page}")

    url = base_url.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")

    for quote in quotes:
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text
        tags = [tag.text for tag in quote.find_all("a", class_="tag")]

        data.append({
            "quote": text,
            "author": author,
            "tags": tags,
            "page": page
        })

print("Всього цитат:", len(data))

with open("full_quotes.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

if response.status_code != 200:
    print("Помилка сторінки:")

if text not in [q["quote"] for q in data]:
    data.append(...)

if text not in [q["quote"] for q in data]:
    data.append(...)

print("Збережено у full_quotes.json")