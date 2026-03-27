from itertools import *


cnt = 0

for i in set(permutations("КОНФЕТЫ ИЛИ ЖИЗНЬ", r=7)):
    i1 = "".join(i)

    if "  " in i1:
        cnt += 1
        print(i1)



print(cnt)