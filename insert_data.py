import sqlite3

conn = sqlite3.connect("quotes.db")
cursor = conn.cursor()

cursor.execute("""
INSERT INTO quotes (text, author)
VALUES (?, ?)
""", ("Test quote", "Bogdan"))

conn.commit()
conn.close()

print("Дані додані")