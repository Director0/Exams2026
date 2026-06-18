from re import *

f = open("27_B.txt")

data = []

for a in f:
    ls = list(map(str, a.split()))

    data.append([float(ls[0]), float(ls[1]), ls[2]])


def dist(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5


def get_cluster(p0):
    clst = [p for p in data if dist(p0, p) <= 1]

    for a in clst:
        data.remove(a)

    clst1 = [get_cluster(p) for p in clst]
    clst += sum(clst1, [])

    return clst


def cen(clst):
    min_dist = 10**21

    for p1 in clst:
        sum_dist = 0

        for p2 in clst:
            sum_dist += dist(p1, p2)

        if sum_dist < min_dist:
            min_dist = sum_dist
            p_min = p1


    return p_min





print(len(data))

clst1 = get_cluster(data[0])
clst2 = get_cluster(data[0])
clst3 = get_cluster(data[0])

cen1 = cen(clst1)
cen2 = cen(clst2)
cen3 = cen(clst3)

print(len(clst1))
print(len(clst2))
print(len(clst3))

print(data)

print(cen1)
print(cen2)
print(cen3)


gc1 = [p for p in clst1 if fullmatch(r"J[0-9]V", p[2])]
gc3 = [p for p in clst3 if fullmatch(r"J[0-9]V", p[2])]
#
b1 = max(gc1, key=lambda x:x[0])[0]
b2 = max(gc3, key=lambda x:x[1])[1]



print(b1)
print(b2)


print(int(b1 * 10000))
print(int(b2 * 10000))