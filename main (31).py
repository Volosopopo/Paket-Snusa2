a = 1
b = 1
N = 10
for i in range(N, 0, -1):
    a *= i
    b += a
    b /= a
    print(b)