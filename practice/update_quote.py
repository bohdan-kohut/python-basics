import sqlite3

quote_id = input("ID Цитати для зміни: ")
new_text = input("Новий текст: ")

conn = sqlite3.connect("quotes.db")
cursor = conn.cursor()

cursor.execute("""
UPDATE quotes
SET text = ?
WHERE id = ?
""", (new_text, quote_id))

conn.commit()
conn.close()

print("Цитата оновлена")