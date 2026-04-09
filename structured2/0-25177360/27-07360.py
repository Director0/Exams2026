f = open("27A.txt")

data = []

for a in f:
    ls = list(map(float, a.split()))
    data.append(ls)


def dist(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5


def get_cluster(p0, d1):
    clst = [p for p in data if dist(p0, p) <= d1]

    for a in clst:
        data.remove(a)

    clst1 = [get_cluster(p, d1) for p in clst]
    clst += sum(clst1, [])

    return clst


def cen(clst):
    min_dist = 10**22

    for p1 in clst:
        sum_dist = 0

        for p2 in clst:
            sum_dist += dist(p1, p2)


        if sum_dist < min_dist:
            min_dist = sum_dist
            p_min = p1


    return p_min


print(len(data))

clst1 = [p for p in data if 0 <= p[1] <= 5]
clst2 = [p for p in data if 0 <= p[0] <= 5 and p[1] > 5]
clst3 = [p for p in data if 5 <= p[0] <= 10 and p[1] > 5]

cen1 = cen(clst1)
cen2 = cen(clst2)
cen3 = cen(clst3)


print(len(clst1))
print(len(clst2))
print(len(clst3))

print(cen1)
print(cen2)
print(cen3)

px = (cen1[0] + cen2[0] + cen3[0]) / 3
py = (cen1[1] + cen2[1] + cen3[1]) / 3

print(px)
print(py)

print(int(abs(px * 100000)))
print(int(abs(py * 100000)))