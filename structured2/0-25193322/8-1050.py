from itertools import *
from re import *

cnt = 0

# for i in product("0123456789ABCDEF", repeat=15):
#     i1 = "".join(i)
#
#     for x in "02468ACE":
#         i2 = i1.replace(x, "*")
#
#     for x in "13579BDF":
#         i2 = i1.replace(x, "$")
#
#     if i1[0] != "0" and (i2 == "*$*$*$*$*$*$*$*" or i2 == "$*$*$*$*$*$*$*$") and i1 == sorted(i1, reverse=True):
#         print(i1, sorted(i1, reverse=True))
#         cnt += 1

# for i1 in "13579BDF":
#     for i2 in "02468ACE":
#         for i3 in "13579BDF":
#             for i4 in "02468ACE":
#                 for i5 in "13579BDF":
#                     for i6 in "02468ACE":
#                         for i7 in "13579BDF":
#                             for i8 in "02468ACE":
#                                 for i9 in "13579BDF":
#                                     for i10 in "02468ACE":
#                                         for i11 in "13579BDF":
#                                             for i12 in "02468ACE":
#                                                 for i13 in "13579BDF":
#                                                     for i14 in "02468ACE":
#                                                         for i15 in "13579BDF":
#                                                             sl = i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8 + i9 + i10 + i11 + i12 + i13 + i14 + i15
#
#                                                             if sl == sorted(sl, reverse=True):
#                                                                 cnt += 1
#                                                                 print(sl)
#
# print(cnt

from math import *


for x in range(1, 100000):
    # print(1000 * 0.7 * log(192 + x, 2))
    if ceil(0.7 * ceil((1000 * ceil(log(192 + x, 2))) / 8))> 1024:
        print(x - 1)
        break