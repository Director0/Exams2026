from itertools import *

s1 = "56 35 2456 36 123678 13459 589 57 67".split()
s2 = "АЕ АИ ЕД ЕМ ДМ МГ ГК ЕК КИ ИЕ КВ ВИ БЕ БК".split()

print(* range(1,10))

for p in permutations("АБЕИВКМДГ"):
    if all(str(p.index(x)+1) in s1[p.index(y)] for x, y in s2):
        print(*p)