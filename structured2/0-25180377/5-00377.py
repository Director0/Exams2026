from itertools import *

cnt = 0

for n in range(800, 901):
    pb = [int("".join(x)) for x in permutations(str(n), r=2) if len(str(int("".join(x)))) >= 2]

    if max(pb) - min(pb) == 30:
        cnt += 1
        print(n, pb)


print(cnt)