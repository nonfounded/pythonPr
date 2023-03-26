import random


def tractor(x):
    price = [0] + [random.randint(-5, 10)
                   for _ in range(x)]
    print(price)
    F = [0] * (x + 1)
    F[1] = price[1]
    for i in range(2, x + 1):
        F[i] = min(F[i - 1], F[i - 2]) + price[i]

    print(F[x])
    way = []
    i = x
    while i > 0:
        way.append(i)
        if F[i - 1] < F[i - 2]:
            i -= 1
        else:
            i -= 2
    way.append(0)
    print(way[::-1])


tractor(5)
