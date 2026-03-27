from sys import setrecursionlimit
from functools import lru_cache

setrecursionlimit(100000000)


@lru_cache(maxsize=None)
def f(x, y):
    if x == 0:
        return y + 1
    if y == 0:
        return f(x - 1, 1)

    return f(x - 1, f(x, y - 1))


for x in range(4):
    for y in range(12):
        print(x, y, f(x, y))

print(f(3, 11))