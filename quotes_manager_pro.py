import sqlite3
import requests
from bs4 import BeautifulSoup
import time

DB_NAME = "quotes.db"


def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS quotes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT UNIQUE,
        author TEXT
    )
    """)

    conn.commit()
    conn.close()


def parse_quotes():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    base_url = "https://quotes.toscrape.com/page/{}/"

    for page in range(1, 4):
        print(f"Парсинг сторінки {page}")

        response = requests.get(base_url.format(page))

        if response.status_code != 200:
            print("Помилка сторінки")
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all("div", class_="quote")

        for quote in quotes:
            text = quote.find("span", class_="text").text
            author = quote.find("small", class_="author").text

            try:
                cursor.execute(
                    "INSERT INTO quotes (text, author) VALUES (?, ?)",
                    (text, author)
                )
            except sqlite3.IntegrityError:
                pass

        time.sleep(1)

    conn.commit()
    conn.close()
    print("Парсинг завершено")


def show_all():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT id, text, author FROM quotes")
    rows = cursor.fetchall()

    if not rows:
        print("База порожня")
    else:
        for row in rows:
            print(f"ID: {row[0]}")
            print(f"Цитата: {row[1]}")
            print(f"Автор: {row[2]}")
            print("-" * 40)

    conn.close()


def search_by_author():
    author = input("Введи автора: ")

    conn = sqlite3.connect(DB_NAME)  # ❗ було sqlite3/connect
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, text, author FROM quotes WHERE author = ?",
        (author,)
    )

    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print(f"ID: {row[0]}")
            print(f"Цитата: {row[1]}")
            print(f"Автор: {row[2]}")
            print("-" * 40)
    else:
        print("Нічого не знайдено")

    conn.close()


def search_by_word():
    word = input("Введи слово: ")

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(  # ❗ було cursor_execute
        "SELECT id, text, author FROM quotes WHERE text LIKE ?",
        (f"%{word}%",)  # ❗ додали %
    )

    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print(f"ID: {row[0]}")
            print(f"Цитата: {row[1]}")
            print(f"Автор: {row[2]}")
            print("-" * 40)
    else:
        print("Нічого не знайдено")

    conn.close()


def update_quote():
    quote_id = input("ID цитати: ")
    new_text = input("Новий текст: ")

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE quotes SET text = ? WHERE id = ?",
        (new_text, quote_id)
    )

    conn.commit()
    conn.close()

    print("Цитату оновлено")


def delete_quote():
    quote_id = input("ID цитати: ")

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM quotes WHERE id = ?",
        (quote_id,)
    )

    conn.commit()
    conn.close()

    print("Цитату видалено")


# запуск
create_table()

while True:
    print("\n1 - спарсити сайт")
    print("2 - показати всі")
    print("3 - пошук по автору")
    print("4 - пошук по слову")
    print("5 - змінити цитату")
    print("6 - видалити цитату")
    print("7 - вихід")

    choice = input("Вибір: ")

    if choice == "1":
        parse_quotes()
    elif choice == "2":
        show_all()
    elif choice == "3":
        search_by_author()
    elif choice == "4":
        search_by_word()
    elif choice == "5":
        update_quote()
    elif choice == "6":
        delete_quote()
    elif choice == "7":
        print("Вихід")
        break
    else:
        print("Невірний вибір")