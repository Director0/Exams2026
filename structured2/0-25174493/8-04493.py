from itertools import *

num = 0

for i in product("ГЕКЭ023", repeat=4):
    num += 1
    i1 = "".join(i)
    for a in ["ЕЕ", "ГГ", "ЭЭ", "22", "00", "33"]: i1 = i1.replace(a, "*")

    if i1[0].isdigit() and "*" not in i1:
        print(num, "".join(i), i1)
