from functools import lru_cache
from sys import setrecursionlimit


@lru_cache(maxsize=None)
def f(n):
    if n == 2022:
        return 52365573

    if n == 1:
        return 1

    if n > 1:
        return 2 * n * f(n - 1)


for n in range(2023):
    f(n)

print((f(2024) / 16 - f(2023)) / f(2022))