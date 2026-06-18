
def f(x, a1, a2):
    p = 254 <= x <= 800
    q = 410 <= x <= 823
    a = a1 <= x <= a2

    return (p and (not a)) <= q


rs = set()

for a1 in range(250, 850):
    for a2 in range(a1, 850):
        if all(f(x, a1, a2) for x in [n + 0.5 for n in range(-1000, 1000)]):
            print(a2 - a1, a1, a2)
            rs.add(a2 - a1)


print(min(rs))