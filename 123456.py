a=int(input("Введите дюймы "))
b=2.54
while 10 <= a <= 22:
    c=a*b
    print(c," Значение в см")
    a+=1
else:
    print("Ошибка")