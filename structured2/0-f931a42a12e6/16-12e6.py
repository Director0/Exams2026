import threading
from math import log
from sys import setrecursionlimit
from functools import lru_cache

setrecursionlimit(100000000)

@lru_cache(maxsize=None)
def f(n):
    if n <= 1000:
        print("proceed ok...")
        return n ** (n ** 2)
    else:
        print("processing...")
        return n + 2 * f(n - 2) + 6 * f(n - 6)

print(f(1001))


# print(f(20024) - 2 * f(20022) - 3 * f(20020) + 18 * f(20014))