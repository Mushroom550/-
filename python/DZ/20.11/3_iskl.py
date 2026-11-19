days = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
try:
    day_num = int(input("Введите номер дня: "))
    
    if day_num < 1 or day_num > 7:
        raise IndexError
        
    print(days[day_num - 1])
    
except ValueError:
    print("Введите номер дня")
except IndexError:
    print("Нет такого дня")
finally:
    print("Проверка завершена")