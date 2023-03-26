import random


def braz(s):
    pr = [0] + [random.randint(1, 10) for _ in range(s)]
    stupenka = [0] * (s + 2)
    for a in range(2, s + 1):
        print(pr[a - 1], pr[a - 2])
        stupenka[a] += min(pr[a - 1], pr[a - 2])
    print(stupenka[-1])


braz(int(input()))
