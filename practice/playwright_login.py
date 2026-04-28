from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://quotes.toscrape.com/login")

    page.fill('input[name="username"]', "admin")
    page.fill('input[name="password"]', "admin")
    page.click('input[type="submit"]')

    page.wait_for_timeout(1000)

    if page.locator('a[href="/logout"]').count() > 0:
        print("Логін успішний")
    else:
        print("Логін неуспішний")

    browser.close()

