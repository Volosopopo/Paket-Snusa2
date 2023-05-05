from random import random
r = round(random() * 100)
i = 1
print("Компьютер загадал число. Отгадайте его. У вас 10 попыток")
while i <= 10:
    a = int(input(str(i) + "-я попытка: "))
    if a > r:
        print("Много")
    elif a < r:
        print("Мало")
    else:
        print("Вы угадали")
        break
    i += 1
else:
    print("Вы исчерпали 10 попыток. Было загадано", n)