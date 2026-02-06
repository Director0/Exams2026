from itertools import *

num = 0

for i in product("АЕКНОТ", repeat=7):
    num += 1

    if num % 2 != 0 and i in permutations("КОТЕНОК"):
        print(num)