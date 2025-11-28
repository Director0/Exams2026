from itertools import *

cnt = 0

for i in permutations("АРТЁМ", r = 5):
    if i[0] not in "АЁ" and i[-1] not in "АЁ":
       cnt += 1


print(cnt)