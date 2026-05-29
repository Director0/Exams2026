for n in range(1, 1000):
    n1 = f"{278:b}"
    n2 = f"{n:b}"

    if f"{(278 | n):b}".count("1") == 7:
        print(n)