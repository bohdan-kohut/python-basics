from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    
    context = browser.new_context(storage_state="session.json")
    page = context.new_page()

    page.goto("https://quotes.toscrape.com/")

    if page.locator('a[href="/logout"]').count() > 0:
        print("Ти вже залогінений через session.json")
    else:
        print("Сесія не спрацювала")

    browser.close()