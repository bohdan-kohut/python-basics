users = [
    {"name": "Bohdan", "age": 31, "city": "Kyiv"},
    {"name": "Ivan", "age": 21, "city": "Lviv"}
]

search_name = input("Введи ім'я: ")

found = False

for user in users:
    if user["name"] == search_name:
        print("Користувача знайдено:", user)
        found = True
        break

if not found:
    print("Користувача не знайдено")