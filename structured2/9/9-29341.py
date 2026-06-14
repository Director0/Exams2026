from itertools import *

f = open("9_29341.txt")

cnt = 0

for s in f:
    ls = sorted(list(map(int, s.split())))

    if ls[-1] < sum(ls[:3]) and all(sum(p[:2]) != sum(p[-2:]) for p in permutations(ls)):
        cnt += 1


print(cnt)