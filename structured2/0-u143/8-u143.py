from itertools import *

res = set()

cnt = 0

for i in permutations("МАЛИНА", r=5):
    res.add("".join(i))


print(len(res))