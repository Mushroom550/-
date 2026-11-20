list_1 = input("Введите текст: ")

list_2 = list_1.lower()

empty_strok = ""
for i in list_2:
    if i.isalnum():
        empty_strok += i

list_2 = list_1[::-1]
if list_1 == list_2:
    print("Это палиндром")
else:
    print("Не палиндром")
