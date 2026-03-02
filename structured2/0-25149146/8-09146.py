from itertools import *

for r1 in range(1, 9):
    num = 0

    for i in product(sorted("НИКУАЙЛД"), repeat=r1):
        num += 1

        if (num == 5350) and (i.count("Н") + i.count("К") + i.count("Й") + i.count("Л") + i.count("Д") > i.count("И") + i.count("У") + i.count("А")) and len([x for x in i if i.count(x) > 1]) == 0:
            print(r1)