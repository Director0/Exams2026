from functools import lru_cache
from sys import setrecursionlimit

def f(n):
    if n >= 2073:
        return n + 3

    if n < 2073:
        return n + f(n + 2) - f(n + 3)


print(f(2070) + f(2069))