from itertools import *

n = 0

for i in product("АЕКНОТ", repeat=7):
    n += 1

    if n % 2 != 0 and i in permutations("КОТЕНОК"):
        print(n)