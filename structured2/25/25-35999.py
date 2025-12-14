for m in range(0, 1000, 2):
    for n in range(1, 1000, 2):
        n1 = 2 ** m * 3 ** n

        if 200_000_000 <= n1 <= 400_000_000:
            print(n1)

