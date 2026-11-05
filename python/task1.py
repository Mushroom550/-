import random

numbers = []
for i in range(10):
    numbers.append(random.randint(-10, 10))

print(numbers)

sum_n = 0
for num in numbers:
    if num < 0:
        sum_n += num
print("Сумма отрицательных чисел:", sum_n)

sum_chet = 0
for num in numbers:
    if num % 2 == 0:
        sum_chet += num
print("Сумма четных чисел:", sum_chet)

sum_nechet = 0
for num in numbers:
    if num % 2 != 0:
        sum_nechet += num
print("Сумма нечетных чисел:", sum_nechet)

p_indx_3 = 1
for j in range(len(numbers)):
    if j % 3 == 0:
        p_indx_3 *= numbers[i]
print("Произведение элементов с индексами кратными 3:", p_indx_3)

min_el = min(numbers)
max_el = max(numbers)
indx_min = numbers.index(min_el)
indx_max = numbers.index(max_el)

if indx_min < indx_max:
    start_indx = indx_min
    end_indx = indx_max
else:
    start_indx = indx_max
    end_indx = indx_min

min_max = 1

if end_indx - start_indx > 1:
    for i in range(start_indx + 1, end_indx):
        min_max *= numbers[i]
    print("Произведение элементов между min и max:", min_max)
else:
    print("Между минимальным и максимальным элементами нет других элементов")

first_el = -1
last_el = -1


for i in range(len(numbers)):
    if numbers[i] > 0:
        if first_el == -1: 
            first_el = i
        last_el = i

sum_p = 0

if first_el != -1 and last_el != -1 and first_el != last_el:
    for i in range(first_el + 1, last_el):
        sum_p += numbers[i]
    print("Сумма элементов между первым и последним положительными:", sum_p)
else:
    print("В списке меньше двух положительных элементов")




