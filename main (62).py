from math import pi, sin, cos

arr = [int(x) for x in "0123456789"]
for y in "0123456789":
    if y != "0":
        for c in "0123456789":
            arr.append(int(y+c))
            for v in "0123456789":
                arr.append(int(y+c+v))
arr = sorted(arr)
arr = str(arr)

a = input("Введите значение x: ")

while a not in arr or a == "":
        if a == "":
            a = input("Вы ничего не ввели, попробуйте еще раз: ")
        else:
            a = input("Неверный тип данных, ведите значение в числовом типе: ")

a = int(a)
if a <= pi / 4:
    print(f"y = sinx  y = {sin(a)}")
else:
    print(f"y = cosx  y = {cos(a)}")