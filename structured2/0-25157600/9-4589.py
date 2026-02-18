from itertools import *

f = open("9_4589.txt")

cnt = 0

for s in f:
    ls = sorted(list(map(int, s.split())))

    if (ls[3] < (ls[0] + ls[1] + ls[2])) and any((x[0] + x[1]) == (x[2] + x[3]) for x in permutations(ls)):
        cnt += 1

print(cnt)