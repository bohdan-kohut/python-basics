numbers = []

for i in range(5):
    num = int(input("Введи число:"))
    numbers.append(num)

print("Твій список:", numbers)
print("Сума:", sum(numbers))