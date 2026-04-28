class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

users = [
    User("Bohdan", 31),
    User("Ivan", 21)
]

for user in users:
    print(user.name, user.age)