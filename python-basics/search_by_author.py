import sqlite3

author = input("Введи автора: ")

conn = sqlite3.connect("quotes.db")
cursor = conn.cursor()

cursor.execute("""
SELECT text, author FROM quotes
WHERE author = ?
""", (author,))

rows = cursor.fetchall()

if rows:
    for row in rows:
        print("Цитата:", row[0])
        print("Автор:", row[1])
        print("-" * 30)

else:
    print("Нічого не знайдено")

conn.close()