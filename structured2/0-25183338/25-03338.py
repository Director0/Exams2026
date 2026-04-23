from re import fullmatch

for n in range(1996, 10**10, 1996):
    if fullmatch(r"1592[02468]*6[0-9]8", str(n)):
        print(n, n // 1996)