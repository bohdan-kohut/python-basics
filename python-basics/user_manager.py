users = []

while True:
    print("1 - додати")
    print("2 - показати")
    print("3 - вийти")

    choice = input("Вибір: ")

    if choice == "1":
        name = input("Ім'я: ")
        age = int(input("Вік: "))

        user = {
            "name": name,
            "age": age
        }

        users.append(user)

    elif choice == "2":
        for user in users:
            print(user)

    elif choice == "3":
        break

    else:
        print("Невірний вибір")