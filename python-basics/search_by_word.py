import sqlite3

word = input("Введи слово для пошуку: ")

conn = sqlite3.connect("quotes.db")
cursor = conn.cursor()

cursor.execute("""
SELECT text, author FROM quotes
WHERE text LIKE ?
""", (f"%{word}%",))

rows = cursor.fetchall()

if rows:
    for row in rows:
        print("Цитата:", row[0])
        print("Автор:", row[1])
        print("-" * 30)
else:
    print("Нічого не знайдено")

conn.close()