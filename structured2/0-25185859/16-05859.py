from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(1000000000)

@lru_cache(maxsize=None)
def f(n):
    if n <= 1:
        return n

    if n > 1 and n % 3 == 0:
        return n + f(n / 3)

    if n > 1 and n % 3 != 0:
        return n + f(n + 3)


print(f(2))