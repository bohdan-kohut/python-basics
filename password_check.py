password = "12345"

for i in range(3):
    user_input = input("Введи пароль:")

    if user_input == password:
        print("Доступ дозволено")
        break
    else:
        print("Неправильний пароль")

else:
    print("Доступ заборонено")