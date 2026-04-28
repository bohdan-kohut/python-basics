numbers = [5, 12, 7, 20, 3, 15]

filtered = []

for num in numbers:
    if num > 10:
        filtered.append(num)

print("Числа більші > 10:", filtered)

numbers = [6, 23, 10, 14, 1, 300]

filtered = []

for num in numbers:
    if num < 300:
        filtered.append(num)

print("Числа меньші < 300:", filtered)