def f(x, a1, a2):
    p = 25 <= x <= 240
    q = 175 <= x <= 300
    r = 270 <= x <= 340
    a = a1 <= x <= a2

    return (q <= p) or ((not a) <= r)

res = []

for a1 in range(25, 340):
    for a2 in range(a1 + 1, 340):
        if all(f(x, a1, a2) for x in range(-10000, 10000)):
            res.append(a2 - a1)
            print(a2 - a1, a1, a2)


print(res)
print(min(res))