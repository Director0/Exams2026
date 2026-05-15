from fnmatch import fnmatch

for n in range(68, 10**9, 68):
    if fnmatch(str(n), "12345?7?8"):
        print(n, n // 68)