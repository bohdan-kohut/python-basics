a = float(input("Перше число: "))
operation = input("Операція (+, -, *, /): ")
b = float(input("Друге число: "))

if operation == "+":
    print("Результат:", a + b)
elif operation == "-":
    print("Результат:", a - b)
elif operation == "*":
    print("Результат:", a * b)
elif operation == "/":
    if b != 0:
        print("Результат:", a / b)
    else:
        print("Помилка: ділення на нуль")
else:
    print("Невідома операція")