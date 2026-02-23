from math import log

from sys import setrecursionlimit
from functools import lru_cache

setrecursionlimit(10000000)

@lru_cache(maxsize=None)
def f(n):
    if n < 2:
        return 7

    if n > 1:
        return 7 * f(n - 2)


print(log(f(8), 7))