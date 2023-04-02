import random


def n_value(values: set, number: int):
    s_v = sorted(values)
    print(s_v)
    for i in range(len(s_v)):
        if number < s_v[i]:
            print(s_v[i], s_v[i - 1])
            return s_v[i - 1] if abs(s_v[i] - number) >= \
                                 abs(s_v[i - 1] - number) else s_v[i]


x = set([random.randint(-10000, 10000) for _ in range(100)])
print(n_value(x, 12))
