import random

x = [random.randint(-10000, 10000) for i in range(5)]
print(sorted(x, key=lambda i: (i % 3)*9999+i))
