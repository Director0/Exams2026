from functools import lru_cache
import sys

sys.setrecursionlimit(5000)

@lru_cache(maxsize=None)
def f(n):
    if n > 10000:
        return n
    elif n < 10001:
        return 5 * f(n + 3)


print(f(4625) / f(4640))