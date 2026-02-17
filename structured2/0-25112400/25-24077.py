from fnmatch import *

for n in range(2026, 10**10 + 1, 2026):
    if fnmatch(str(n), "431*7?14"):
        print(n, n // 2026)