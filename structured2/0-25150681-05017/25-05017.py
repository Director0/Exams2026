from fnmatch import *

for n in range(2024, 10**10, 2024):
    if fnmatch(str(n), "1*2322?2"):
        print(n, n // 2024)