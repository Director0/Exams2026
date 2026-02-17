from itertools import *

num = 0

for i in product(sorted("БУРАТИНО"), repeat=5):
    num += 1

    if num % 2 != 0 and i[0] not in "УАИО" and len([x for x in i if i.count(x) > 1]) == 0:
        print(num, i)