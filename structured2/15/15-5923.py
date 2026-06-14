def f(x, a1, a2):
    p = 5 <= x <= 280
    q = 295 <= x <= 400
    r = 375 <= x <= 450
    a = a1 <= x <= a2

    return (q <= p) or ((not a) <= r)


rs = set()

for a1 in range(4, 540):
    for a2 in range(a1, 540):
        if all(f(x, a1, a2) for x in [x + 0.5 for x in range(-500, 1000)]):
            rs.add(a2 - a1)
            print(a2 - a1, a1, a2)


print(min(rs))