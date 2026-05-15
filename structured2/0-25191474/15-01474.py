
def f(x, a1, a2):
    b = 25 <= x <= 40
    c = 12 <= x <= 33
    a = a1 <= x <= a2

    return (b <= a) and ((not c) or a)


ls = []

for a1 in range(1, 1000):
    for a2 in range(a1, 1000):
        if all(f(x, a1, a2) for x in range(-1000, 1000)):
            print(a2 - a1, a1, a2)
            ls.append(a2 - a1)


print(min(ls))