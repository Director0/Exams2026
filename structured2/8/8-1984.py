from itertools import *

cnt = 0

for i in permutations("ИГРОК", r = 5):
    i0 = "".join(i)

    if i0[0] != "К" and "РОК" not in i0:
        cnt += 1


print(cnt)