f = open("27_A_23571.txt")

data = [[float(x) for x in s.split()] for s in f]

def dist(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5

def cen(cl):
    res = []

    for p1 in cl:
        sd = sum(dist(p1, p2) for p2 in cl)
        res.append([sd, p1])

    return min(res)[1]

cl1, cl2 = [], []

for s in data:
    x, y = s

    if y < 10:
        cl1.append([x, y])
    else:
        cl2.append([x, y])


print(len(cl1), len(cl2), len(data))

cen1, cen2 = cen(cl1), cen(cl2)

print(int(abs(cen1[0] + cen2[0]) * 10000), int(abs(cen1[1] + cen2[1]) * 10000))