for x in "0123456789AB":
    n1 = "9" + x + "AB"
    n2 = x + "46C"
    n3 = "B7" + x

    if (int(n1, 13) + int(n2, 16) - int(n3, 15)) % 14 == 0:
        print((int(n1, 13) + int(n2, 16) - int(n3, 15)) // 14)
