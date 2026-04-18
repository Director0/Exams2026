from sys import setrecursionlimit
from functools import lru_cache

setrecursionlimit(1000000)

rs = []

for a in range(100):
    for b in range(100):
        for c in range(100):
            if 3**a * 2**b + c == 9217:
                rs.append(a + b + c)

print(min(rs))