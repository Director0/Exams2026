alb = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


for x in "0123456789ABCDEFGHIJKLMNO":
    n1 = int(f"A4{x}7F2", 25)
    n2 = int(f"N{x}G5{x}H", 25)
    n3 = int(f"74{x}M26", 25)

    if (n1 + n2 + n3) % 24 == 0:
        print(x, (n1 + n2 + n3) / 24)