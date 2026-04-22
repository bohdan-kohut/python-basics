from playwright.sync_api import sync_playwright
import json

data = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://quotes.toscrape.com/")

    for i in range(3):
        quotes = page.locator(".quote").all()

        for quote in quotes:
            text = quote.locator(".text").inner_text()
            author = quote.locator(".author").inner_text()

            data.append({
                "quote": text,
                "author": author
            })

        next_button = page.locator(".next.a")
        if next_button.count() > 0:
            next_button.click()
        else:
            break

    browser.close()

with open("playwright_quotes.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print("Дані збережено у playwright_quotes.json")
print("Кількість цитат:", len(data))