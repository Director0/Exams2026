from itertools import *

cnt = 0

for i in set(permutations("BBBBRRRGG", r=9)):
    i1 = "".join(i)

    if "BB" not in i1 and "RR" not in i1 and "GG" not in i1:
        print(i1)
        cnt += 1


print(cnt)