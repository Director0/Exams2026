from sys import setrecursionlimit
from functools import lru_cache


@lru_cache(maxsize=None)
def f(n):
    if n == 1:
        return 1

    if n > 1:
        return n + f(n - 1)


for n in range(1, 2025):
    f(n)

cnt = 0

for n in range(1, 101):
    if (f(2023) // f(n)) % 2 == 0:
        cnt += 1


print(cnt)