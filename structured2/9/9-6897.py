from itertools import *

f = open("9_6897.txt")

gcnt = 0



for s in f:

    s1 = sorted(list(map(int, s.split())))
    # nums = []

    if s1[-1] < sum(s1[:-1]) and s1[0] + s1[3] != s1[1] + s1[2]:
        gcnt += 1

print(gcnt)