from fnmatch import fnmatch

for n in range(1, 10**10 + 1):
    if n ** 2 <= 10**10 and fnmatch(str(n**2), "4*1?009"):
        print(n, n ** 2)