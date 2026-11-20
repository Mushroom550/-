list_1 = input("Введите текст: ")
words = input("Введите зарезервированные слова: ")
words_1 = words.split()
for i in words_1:
    list_1 = list_1.replace(i, i.upper())
    print("Изменённый текст: ")
    print(list_1)