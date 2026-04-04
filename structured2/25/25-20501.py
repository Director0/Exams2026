from re import *


for n in range(1432, 10**10 + 1, 1432):
    if str(n)[:4] == "8902" and str(n)[6:] in [str(2**x) for x in range(0, 14)]:
        print(n, n // 1432)