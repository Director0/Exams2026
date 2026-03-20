from sys import setrecursionlimit
from functools import lru_cache

setrecursionlimit(100000)

@lru_cache(maxsize=None)
def f(n):
    if n >= 128 and n > 0:
        return f(n - 5) + 1092
    else:
        return 5 * g(n - 7) + 29


@lru_cache(maxsize=None)
def g(n):
    if n > 303728 and n > 0:
        return n - 15
    else:
        return g(n + 8) // 2 - 109


print(f(2049))