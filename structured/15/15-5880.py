def tr(a, b, c):
    mn = sorted([a, b, c])

    if 2 * mn[2] < sum(mn):
        return True
    else:
        return False

def f(x):
    return tr(a, 5, x) <= ((max(x, 11) <= 19) == (not(tr(23, 13, x))))


for a in range(1, 5000):
    if all(f(x) for x in range(1, 5000)):
        print(a)