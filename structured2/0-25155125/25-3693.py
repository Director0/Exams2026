from fnmatch import fnmatch

for n in range(51, 10**6 + 1, 51):
    if fnmatch(str(n), "12*45*"):
        print(n, n // 51)