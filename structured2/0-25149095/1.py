from itertools import *

s1="38 58 146 36 27 347 568 127".split()
s2="de ea ah hc cf fg gb bd eb hg".split()

print(* range(1,9))

for p in permutations ("deahcfgb"):
    if all(str(p.index(x)+1) in s1[p.index(y)] for x , y in s2):
        print(*p)
