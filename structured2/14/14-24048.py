abt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


for p in range(1, 37):
    # n1 = int("KOT", p)
    # n2 = int("GOLODNI", p)
    # n3 = int("MEEOW", p)
    # n4 = int("100", p)

    n1 = (10 + abt.index("K")) * p**2 + (10 + abt.index("O")) * p**1 + (10 + abt.index("T")) * p**0
    n2 = (10 + abt.index("G")) * p**6 + (10 + abt.index("O")) * p**5 + (10 + abt.index("L")) * p**4 + (10 + abt.index("O")) * p**3 + (10 + abt.index("D")) * p**2 + (10 + abt.index("N")) * p**1 + (10 + abt.index("I")) * p**0
    n3 = (10 + abt.index("M")) * p**4 + (10 + abt.index("E")) * p**3 + (10 + abt.index("E")) * p**2 + (10 + abt.index("O")) * p**1 + (10 + abt.index("W")) * p**0
    n4 = 1 * p**2 + 0 * p**1 + 0 * p**0


    if n1 + n2 == n3 * n4 - 20194023088:
        print(p)