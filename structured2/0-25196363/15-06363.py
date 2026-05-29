def f(x, a1, a2):
    p = 10 <= x <= 150
    q = 160 <= x <= 250
    r = 240 <= x <= 300
    a = a1 <= x <= a2

    return (q <= p) or ((not a) <= r)


rs = []

xs = [x + 0.5 for x in range(-500, 500)]

for a1 in range(1, 450):
    for a2 in range(a1, 450):
        if all(f(x, a1, a2) for x in xs):
            print(a2 - a1, a1, a2)
            rs.append(a2 - a1)


print(f"ans: {min(rs)}")