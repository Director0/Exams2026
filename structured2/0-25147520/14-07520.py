def conv(num, n):
    res = ""

    while num != 0:
        res += str(num % n)
        num //= n

    return res[::-1]

for n in range(1, 123132321):
    if (len(conv(n, 6)) == 2) and (len(conv(n, 5)) == 3) and (conv(n, 11)[-1] == 2):
        print(n)