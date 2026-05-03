import warnings
from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(100000000)

@lru_cache(maxsize=None)
def f(n):
    if n < 10:
        return 1
    else:
        return (n + 3) * f(n - 3)


for x in range(1, 250000):
    f(x)


print((f(247563)//519 - 477 * f(247560)) // f(247557))