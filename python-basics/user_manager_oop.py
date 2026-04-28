class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self):
        name = input("Ім'я: ")
        age = int(input("Вік: "))

        user = User(name, age)
        self.users.append(user)

    def show_users(self):
        for user in self.users:
            print(user.name, user.age)

manager = UserManager()

while True:
    print("1 - додати")
    print("2 - показати")
    print("3 - вихід")
    
    choice = input("Вибір: ")

    if choice == "1":
        manager.add_user()
    elif choice == "2":
        manager.show_users()
    elif choice == "3":
        break