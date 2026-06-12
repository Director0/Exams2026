for p in range(16, 38):
    if (int("17496", p) + int("91F83", p) + int("D9543", p)) % 12 == 0:
        print(p, (int("17496", p) + int("91F83", p) + int("D9543", p)) / 12)