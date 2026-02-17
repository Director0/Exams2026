from itertools import *

alb = "123456789ABCDE"

res = set()

for i1 in "2468ACE":
    for i2 in "0369C":
        for i3 in "02468ACE":
            for i4 in "0369C":
                for i5 in "02468ACE":
                    res.add((i1 + i2 + i3 + i4 + i5))


for i1 in "369C":
    for i2 in "02468ACE":
        for i3 in "0369C":
            for i4 in "02468ACE":
                for i5 in "0369C":
                    res.add((i1 + i2 + i3 + i4 + i5))


print(len(res))