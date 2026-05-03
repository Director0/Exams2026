from itertools import *

cnt = 0

for i1 in "2468":
    for i2 in "1357":
        for i3 in "2468":
            for i4 in "1357":
                for i5 in "2468":
                    for i6 in "1357":
                        for i7 in "2468":
                            for i8 in "1357":
                                for i9 in "2468":
                                    for i10 in "1357":
                                        for i11 in "2468":
                                            n = i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8 + i9 + i10 + i11

                                            if all(n.count(x) <= 4 for x in n):
                                                cnt += 1


print(cnt * 2)