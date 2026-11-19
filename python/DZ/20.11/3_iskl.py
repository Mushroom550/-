day = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
try:
    num = int(input("Введите номер дня: "))
    
    if num < 1 or num > 7:
        raise IndexError
        
    print(day[num - 1])
    
except ValueError:
    print("Введите номер дня")
except IndexError:
    print("Нет такого дня")
finally:
    print("Проверка завершена")
