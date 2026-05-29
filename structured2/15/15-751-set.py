p = [1, 2, 4, 8]
q = [1, 2, 3, 4, 5, 6]
a = []


def f(x, a):
    return (x not in a) <= (not ((x in p) or (x in q)))


for x in range(1, 1000):
    if not f(x, a):
        a.append(x)


print(len(a))