from fnmatch import fnmatch


for n in range(8465, 10**10 + 1):
    if (n % 8465 == 0 or n % 9799 == 0) and (fnmatch(str(n), "10*2426?")):
        print(n, n / 8465, n / 9799, n / (8465 * 9799))