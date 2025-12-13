from itertools import *

cnt = 0

for i in permutations("КАБИНЕТ", r=7):
    i1 = "".join(i)

    if i1[-1] not in "АИЕ":
        cnt += 1

print(cnt)