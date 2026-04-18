from itertools import *

rs = set()

for i in product("АБЗРУ", repeat=6):
    i1 = "".join(i)

    if i1.count("А") == 3 and "АА" in i1 and "ААА" not in i1:
        rs.add(i1)
        print(i1)


print(len(rs))