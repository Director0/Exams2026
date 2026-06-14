from itertools import *

cnt = 0

for i in product(range(0, 16), repeat=3):
    ls = [x for x in i]

    if len(ls) == len(set(ls)) and ls == sorted(ls, reverse=True) and sum(ls) <= 15:
        print(ls)
        cnt += 1


print(cnt)