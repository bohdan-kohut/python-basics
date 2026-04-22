from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://quotes.toscrape.com/")

    for i in range(3):
        print(f"Сторінка {i + 1}")

        quotes = page.locator(".text").all_text_contents()
        for quote in quotes:
            print(quote)

        next_button = page.locator(".next a")
        if next_button.count() > 0:
            next_button.click()
        else:
            break

    browser.close()