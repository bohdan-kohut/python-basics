import requests
from bs4 import BeautifulSoup
import sqlite3
import time

conn = sqlite3.connect("quotes.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS quotes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT,
    author TEXT
)
""")

base_url = "https://qoutes.toscrape.com/page/{}/"

for page in range(1,4):
    print(f"Сторінка {page}")

    url = base_url.format(page)
    response = requests.get(url)

    if response.status_code != 200:
        continue

    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")

    for quote in quotes:
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text

         cursor.execute("""
         INSERT INTO quotes (text, author)
         VALUES (?, ?)
         """, (text, author))
    time.sleep(1)

conn.commit()
conn.close()

print("Дані збережені в БЗ")



