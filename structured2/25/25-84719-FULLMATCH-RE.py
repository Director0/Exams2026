from re import *

for n in range(2026, 10**10, 2026):
    if fullmatch(r"5[13579]34[13579]71\d*2", str(n)):
        print(n)