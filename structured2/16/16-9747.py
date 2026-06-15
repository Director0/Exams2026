from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(10000000)

@lru_cache(maxsize=None)
def f(n):
    if n < 11:
        return n
    if n >= 11:
        return n + f(n - 1)

for n in range(1, 2050):
    f(n)


print(f(2024) - f(2021))