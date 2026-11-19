try:
    num = int(input("Введите целое число: "))
    print(num ** 2)
except ValueError:
    print("Введите целое число")