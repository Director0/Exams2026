from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(10000000)

# @lru_cache(maxsize=None)
# def f(n):
#     if n > 100000:
#         return n
#     else:
#         return f(n + 1) + 5*n + 2


ls = [0] * 100_003
ls[100002] = 100_002
ls[100001] = 100_001

for i in range(100_000, 0, -1):
    ls[i] = ls[i + 1] + 5 * i + 2



print(ls[3] - ls[7])