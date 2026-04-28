import requests
from bs4 import BeautifulSoup

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

for item in data:
    print("Цитата:", item["quote"])
    print("Автор:", item["author"])
    print("-" * 30)