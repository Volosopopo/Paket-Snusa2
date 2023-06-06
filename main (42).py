def is_prime(x):
    if x % 2 == 0 and x !=2:
        return False
    else:
        return True
    if x == 0 or x == 1:
        return False
    else:
        return True
    for a in range(3, int(sqrt(x).real) + 1, 2):
        if x % a == 0:
            return False
    return True
a=int(input('Введите число '))
print(is_prime(a))