m = 1917

for n in range(m, 10**10, m):
    s = str(n)

    if s[0] == "3" and s[2:4] == "12" and s[5:7] == "14" and s[-1] == "5":
        print(n, n // m)