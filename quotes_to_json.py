import requests
from bs4 import BeautifulSoup
import json

url = "https://quotes.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

data = []

for i in range(len(quotes)):
    item = {
        "quote": quotes[i].text,
        "author": authors[i].text
    }
    data.append(item)

with open("quotes.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print("Дані збережено в quotes.json")
