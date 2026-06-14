from itertools import *
from string import *

num = 0

# for i in product("ABCDEFGHIJKLMNOPQRSTUVWXYZ", repeat=8):
#     num += 1
#
#     i1 = "".join(i)
#
#     if i1 == "INFINITY":
#         print(num, i1, num + 8353082582)


n1 = ascii_uppercase.index("I") * 26**7 + ascii_uppercase.index("N") * 26**6 + ascii_uppercase.index("F") * 26**5 + ascii_uppercase.index("I") * 26**4 + ascii_uppercase.index("N") * 26**3 + ascii_uppercase.index("I") * 26**2 + ascii_uppercase.index("T") * 26**1 + ascii_uppercase.index("Y")

print(8353082582 + n1 + 1)