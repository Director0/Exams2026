from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(1000000000)



@lru_cache(maxsize=None)
def f(curr, end):
    if curr > end or curr == 100:
        return 0
    if curr == end:
        return 1


    if curr % 10 == 0 and curr % 68 == 0:
        return f(curr**2, end)
    elif curr % 10 == 0:
        return f(curr + (curr % 68), end) + f(curr**2, end)
    elif curr % 68 == 0:
        return f(curr + (curr % 10), end) + f(curr**2, end)
    else:
        return f(curr + (curr % 10), end) + f(curr + (curr % 68), end) + f(curr**2, end)


print(f(2, 68) * f(68, 680))