from sys import setrecursionlimit
from functools import lru_cache

setrecursionlimit(100000000)

@lru_cache(maxsize=None)
def f(n):
    if n < 10:
        return 3
    else:
        return (n + 4) * f(n - 5)

for n in range(100, 300000, 1057):
    f(n)


print((f(257487)//683 + 67*f(257477))//f(257472))