class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(self.name, self.age)

user1 = User("Bohdan", 31)
user1.show_info()