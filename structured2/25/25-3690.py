from fnmatch import fnmatch


ls = [x for x in range(10, 100) if fnmatch(str(x), "?2")]


for n in range(103050608, 10**9 + 1):
    l1 = [x for x in ls if n % x == 0]
    if fnmatch(str(n), "1?3?5?6?8") and len(l1) >= 5:
        print(n, n // min(l1))