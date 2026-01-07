alb = "0123456789AB"

def conv(num, n):
    res = ""

    while num != 0:
        res += alb[(num % n)]
        num //= 12

    return res[::-1]

res1 = []

for n in range(1, 1000):
    n12 = conv(n, 12)

    if n % 3 == 0:
        n12 = "1" + n12 + "B"
    else:
        n12 = "2" + n12 + "0"

    r = int(n12, 12)

    if r < 1996:
        res1.append([r, n])

print(sorted(res1))
print(max(res1))