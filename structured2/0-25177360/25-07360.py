from re import *

for n in range(1777, 10**10 + 1, 1777):
    if fullmatch(r"21[0-9]{3}68[0-9]79", str(n)):
        print(n, n // 1777)