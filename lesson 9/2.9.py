import random


def braz(s):
    pr = [0,0] + [random.randint(1, 10) for _ in range(s)]
    print(pr)
    #stupenka = [0] * (s + 4)
    for a in range(2, s + 2):
        pr[a] += min(pr[a - 1], pr[a - 2])
    print(pr[-1])


braz(int(input()))
