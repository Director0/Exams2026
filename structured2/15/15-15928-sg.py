def f(x, y, a1, a2):
    ax = a1 <= x <= a2
    ay = a1 <= y <= a2

    return (ax <= (x**2 <= 81)) and ((y**2 <= 36) <= ay)

maxl = -10**21

for a1 in range(-100, 100):
    for a2 in range(a1 + 1, 100):
        if all(f(x, y, a1, a2) for x in range(-100, 100) for y in range(-100, 100)):
            maxl = max(maxl, a2 - a1)


print(maxl)