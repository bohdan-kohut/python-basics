import sqlite3

def show_all():
    conn = sqlite3.connect("quotes.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM quotes")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()

def delete_quote():
    quote_id = input("ID для видалення: ")

    conn = sqlite3.connect("quotes.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM quotes WHERE id = ?", (quote_id,))
    conn.commit()
    conn.close()

    print("Видалено")

def update_quote():
    quote_id = input("ID для зміни")
    new_text = input("Новий текст")

    conn = sqlite3.connect("quotes.db")
    cursor = conn.cursor()

    cursor.execute("UPDATE quotes SET text = ? WHERE id = ?", (new_text, quote_id))
    conn.commit()
    conn.close()

    print("Оновлено")

while True:
    print("1 - показати всі")
    print("2 - видалити")
    print("3 - змінити")
    print("4 - вихід")

    choice = input("Вибір:")

    if choice == "1":
        show_all()
    elif choice == "2":
        delete_quote()
    elif choice == "3":
        update_quote()
    elif choice == "4":
        break
