def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

# Приклад використання функції
num = int(input("Введи число:"))

if is_even(num):
    print("Число парне")
else:
    print("Число непарне")