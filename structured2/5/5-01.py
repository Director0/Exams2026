def conv(num, n):
    res = ""

    while num != 0:
        res += str(num % n)
        num //= n

    return res[::-1]

res1 = []

for n in range(4, 1000):
    n1 = conv(n, 3)

    if str(n)[-2:] == "10":
        n1 = "2" + n1
    else:
        n1 = "1" + n1

    r = int(n1, 3)

    if r > 130:
        res1.append([n, r])

print(res1)
print(min(res1))