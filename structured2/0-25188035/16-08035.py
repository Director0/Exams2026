from functools import lru_cache
from sys import setrecursionlimit


setrecursionlimit(100000000)


@lru_cache(maxsize=None)
def f(n):
    if n == 0:
        return 1

    return f(n - 1) * n


for n in range(100, 400000, 1009):
    print(n)
    f(n)

print(f(400000))