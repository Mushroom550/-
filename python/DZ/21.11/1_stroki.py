list_1 = input("Введите текст: ")

list_2 = list_1.lower()

empty_strok = ""
for i in list_2:
    if i.isalnum():
        empty_strok += i

revers = empty_strok[::-1]
if empty_strok == revers:
    print("Это палиндром")
else:
    print("Не палиндром")
