def f(x, a1, a2):
    p = 20 <= x <= 85
    q = 30 <= x <= 65
    a = a1 <= x <= a2

    return (p == q) <= (not a)


cnt = 0

for a1 in range(1, 200):
    for a2 in range(a1 + 1, 200):
        if all(f(x, a1, a2) for x in range(1, 1000)):
            print(a2 - a1, a1, a2)
            cnt += 1


print(cnt)