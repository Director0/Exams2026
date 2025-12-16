f = open("27_A_23284.txt")

data = [[float(x) for x in s.split()] for s in f]

print(data)

cl1, cl2, cl3 = [], [], []

for x, y in data:
    if 5 <= x <= 10:
        cl1.append([x, y])
    elif 15 <= x <= 20:
        cl2.append([x, y])
    elif 20 <= x <= 25:
        cl3.append([x, y])

print(len(cl1), len(cl2), len(cl3))

def dist(p1, p2):
    return ((p1[0] - p2[0])**2 + ((p1[1] - p2[1])**2)) ** 0.5

def cen(cl):
    res = []

    for p in cl:
        d = sum(dist(p, t) for t in cl)
        res.append([d, p])

    return min(res)[1]

