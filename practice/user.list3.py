users = [
    {"name": "Bogdan", "age": 31, "city": "Kyiv"},
    {"name": "Ivan", "age": 30, "city": "Lviv"},
    {"name": "Anna", "age": 32, "city": "Odessa"} 
]

for user in users:
    print(user["name"], user["age"], user["city"])
    if user["age"] > 25:
        print("Ці користувачі старші за 25 років")