sum=0
maxx = 0
minn = 0
k = 0
while True: 
    b=int(input("Введите число: "))
    if b==7:
        print("Good bye!")
        break
    sum = sum+b   
    if k == 0:
        maxx = b  
        minn = b
    else:
        if b>maxx:
            maxx = b
        if b<minn:
            minn = b
    k = k+1
    print("Сумма:", sum, "макс:", maxx, "мин:", minn)
    
