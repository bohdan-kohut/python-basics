import sqlite3

quote_id = input("ID цитати для виведення: ")

conn = sqlite3.connect("quotes.db")
cursor = conn.cursor()

cursor.execute("""
DELETE FROM quotes
WHERE id = ?
""", (quote_id,))

conn.commit()
conn.close()

print("Цитата видалена")