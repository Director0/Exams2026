from fnmatch import fnmatch

m = 1917

for n in range(m, 10**10, m):
    s = str(n)

    if fnmatch(s, "3?12?14*5"):
        print(n, n // m)