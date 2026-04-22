from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://quotes.toscrape.com/")

    quotes = page.locator(".text").all_text_contents()

    for quote in quotes:
        print(quote)

    browser.close()