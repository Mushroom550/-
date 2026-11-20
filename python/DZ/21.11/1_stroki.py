list_1 = input("Введите текст: ")
list_1.split(" ")
list_2 = list_1.lower()
list_2 = list_1[::-1]
if list_1 == list_2:
    print("Это палиндром")
else:
    print("Не палиндром")