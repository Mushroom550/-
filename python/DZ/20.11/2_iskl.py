try:
    a = int(input("Введите первое целое число: "))
    b = int(input("Введите второе целое число: "))
    result = a / b
    print(result)
except ValueError:
    print("Нужны два целых числа")
except ZeroDivisionError:
    print("На ноль делить нельзя")