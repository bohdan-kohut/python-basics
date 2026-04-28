def add_user():
    namne = input("Імя: ")
    age = int(input("Вік: "))

    user = {
        "name": name,
        "age": age
    }

    users.append(user)

    def show_users():
        for user in users:
            print(user)

def find_user():
    name = input("Імя для пошуку: ")

    for user in users:
        if user["name"] == name:
            print("Знайдено:", user)
            return

    print("Не знайдено")


while True:
    print("1 - додати")
    print("2 - показати")
    print("3 - знайти")
    print("4 - вийти")

    choice = input("Вибір: ")

    if choice == "1":
        add_user()
    elif choice == "2":
        show_users()
    elif choice == "3":
        find_user()
    elif choice == "4":
        break
    else:
        print("Помилка")
