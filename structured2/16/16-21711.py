from functools import lru_cache
from sys import setrecursionlimit


@lru_cache(maxsize=None)
def f(n):
    if n < 20:
        return n

    if n >= 20:
        return (n - 6) * f(n - 7)


for n in range(50000):
    f(n)

print((f(47872) - 290 * f(47865))/f(47858))