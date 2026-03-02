from fnmatch import fnmatch

for n in range(151, 10**8, 151):
    if fnmatch(str(n), "10?4??9"):
        print(n, n // 151)