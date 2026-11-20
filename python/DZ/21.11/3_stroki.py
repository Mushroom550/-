list_1 = input("Введите текст: ")
k = 0
for i in list_1:
    if i in ".!?":
        k += 1
print(f"Количество предложений {k}")