import random


numbers = []
for _ in range(10):
    numbers.append(random.randint(-10, 10))

print("Исходный список:", numbers)


chet_numbers = []
nechet_numbers = []
n_numbers = []
p_numbers = []

for num in numbers:
    if num % 2 == 0:
        chet_numbers.append(num)
    else:
        nechet_numbers.append(num)

    if num < 0:
        n_numbers.append(num)
    elif num > 0:
        p_numbers.append(num)

print("Только четные числа:", chet_numbers)
print("Только нечетные числа:", nechet_numbers)
print("Только отрицательные числа:", n_numbers)
print("Только положительные числа:", p_numbers)

