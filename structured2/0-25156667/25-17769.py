from fnmatch import fnmatch

for n in range(2025, 10**10 + 1, 2025):
    if fnmatch(str(n), "21?3*145?5"):
        print(n, n // 2025)