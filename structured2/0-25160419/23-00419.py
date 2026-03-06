import math
from sys import setrecursionlimit
from functools import lru_cache

setrecursionlimit(1000000)

@lru_cache(maxsize=None)
def smp(n):
    dvs = set()

    for i in range(1, int((n**0.5)) + 1):
        if n % i == 0:
            dvs.add(n)
            dvs.add(n // i)

    if len(dvs) == 1:
        return True
    else:
        return False

print(smp(25))

@lru_cache(maxsize=None)
def f(curr, end):
    if curr > end:
        return 0
    if curr == end:
        return 1

    return f(curr + min([x for x in range(curr + 1, curr + 10) if x % 3 == 0]), end) + f(curr + min([x for x in range(curr + 1, curr + 100) if smp(x) == True]), end) + f(curr + min([x for x in range(curr + 1, curr + 2000) if math.log(x, 2) % 1 == 0]), end) + f(curr + (int(str(curr)[-1]) if str(curr)[-1] != "0" else 0), end)


print(f(4, 1228))