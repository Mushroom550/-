a=int(input())
b=int(input())

d,d1=0, 0
e,e1=0, 0
f,f1=0, 0

for i in range(a, b+1):
    if i%2==0:
        d=d+i
        d1=d1+1
    else:
        e=e+i
        e1=e+1
    if i%9==0:
        f=f+i
        f1=f1+1
        
sr_d = 0
sr_e = 0
sr_f = 0

if d1>0:
    sr_d = d/d1
    
if e1>0:
    sr_e = e/e1
    
if f1>0:
    sr_f = f/f1
    
print("Чет: сумма =", d, "ср=", sr_d)
print("Нечет: сумма =", e, "ср=",  sr_e)
print("Крат 9: сумма =", f, "ср=", sr_f)

      
