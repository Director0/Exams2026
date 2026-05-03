from itertools import *

s1 = "4568 345679 25 12679 12369 12458 24 16 245".split()
s2 = "НМ НР НП НС НТ НВ МР РП РК РВ ПС СТ СК СВ ЛК ЛВ КВ".split()

print(* range(1,10))

for p in permutations("ПЛКМВРТСН"):
    if all(str(p.index(x)+1) in s1[p.index(y)] for x, y in s2):
        print(*p)