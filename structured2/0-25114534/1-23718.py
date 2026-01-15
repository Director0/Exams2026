from itertools import *

s1="25 159 78 67 126 457 346 39 28".split()
s2 = "МК КО ОТ ТЛ ЛЕ ЕВ ВУ УЯ ЯМ КТ ЛВ ".split()

print(* range(1,10))

for p in permutations("ЯМКОТЛЕВУ"):
    if all(str(p.index(x)+1) in s1[p.index(y)] for x, y in s2):
        print(*p)