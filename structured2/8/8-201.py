from itertools import *

cnt = 0

for i in permutations("ПЕСКАРЬ"):
    i1 = "".join(i)

    if "Ь" != i1[0] and "ЬЕ" not in i1 and "ЬА" not in i1 and "ЬР" not in i1:
        cnt += 1


print(cnt)
