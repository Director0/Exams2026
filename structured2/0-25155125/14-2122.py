def conv(num, n):
    res = ""

    while num != 0:
        res += str(num % n)
        num //= n

    return res[::-1]


n = 1 * 3**37 + 2 * 3**23 + 3 * 3**20 + 4 * 3**4 + 5 * 3**3 + 4 + 5

n1 = conv(n, 9)

print(n1.count("0"))