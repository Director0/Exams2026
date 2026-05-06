from itertools import *

f = open("9_28755.txt")

cnt = 0

for s in f:
    ls = sorted(list(map(int, s.split())))

    if ls[-1] < sum(ls[:-1]) and len([p for p in set(permutations(ls, r = 4)) if sum(list(p)[:2]) == sum(list(p)[2:])]) == 0:
        cnt += 1


print(cnt)

