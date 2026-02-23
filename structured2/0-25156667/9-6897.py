from itertools import *

f = open("9_6897.txt")

cnt = 0

for s in f:
    ls = sorted(list(map(int, s.split())))

    if (ls[3] < (ls[0] + ls[1] + ls[2])) and not(any((l[0] + l[1]) == (l[2] + l[3]) for l in permutations(ls))):
        cnt += 1

print(cnt)