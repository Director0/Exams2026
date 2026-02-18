from itertools import *

num = 0

for i in product("ИРЩЮ", repeat=5):
    num += 1

    if i[0] == "Щ" and i[-1] == "И":
        print(num, "".join(i))