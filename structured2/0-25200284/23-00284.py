from functools import lru_cache
from sys import setrecursionlimit

ls = set()

def f(curr, m):
    global ls

    if m == 4:
        ls.add(curr)
    else:
        f(curr * 2, m + 1)
        f((curr * 2) + 1, m + 1)

f(1, 0)

print(ls)
print(len(ls))