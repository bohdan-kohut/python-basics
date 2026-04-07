import json

def load_users():
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
            return []

def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file)

users = load_users()

def add_user():
    name = input("Імя: ")
    age = int(input("Вік: "))

    user = {
        "name": name,
        "age": age
    }

    users.append(user)
    save_users(users)

    