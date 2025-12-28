f = open("27_B_23571.txt")

data = [[float(x) for x in s.split()] for s in f]

def dist(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5

def cen(cl):
    res = []

    for p1 in cl:
        sd = sum(dist(p1, p2) for p2 in cl)
        res.append([sd, p1])

    return min(res)[1]

def distmin(cl1, cl2):
    min_dist = 10**20

    for p1 in cl1:
        for p2 in cl2:
            d = dist(p1, p2)

            if d < min_dist:
                min_dist = d

    return min_dist


def distmax(cl1, cl2):
    max_dist = -10 ** 21

    for p1 in cl1:
        for p2 in cl2:
            d = dist(p1, p2)

            if d > max_dist:
                max_dist = d

    return max_dist


cl1, cl2, cl3 = [], [], []

for s in data:
    x, y = s

    if 0 < y < 10:
        cl1.append([x, y])
    elif 10 < y < 15:
        cl2.append([x, y])
    elif 15 < y < 20:
        cl3.append([x, y])


print(len(cl1), len(cl2), len(cl3), len(data))

minres = [distmin(cl1, cl2), distmin(cl2, cl3), distmin(cl1, cl3)]
maxres = [distmax(cl1, cl2), distmax(cl2, cl3), distmax(cl1, cl3)]


print(int(min(minres) * 10000), int(max(maxres) * 10000))
