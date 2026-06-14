def conv(num, n):
    rs = ""
    while num != 0:
        rs += str(num % n)
        num //= n

    return rs[::-1]


for x in range(0, 1000):
    if conv(7**666 + 7**333 + 49**x - 343, 7).count("6") == 49:
        print(x)
