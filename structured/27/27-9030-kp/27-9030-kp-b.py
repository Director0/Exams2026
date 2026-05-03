from re import *

f = open("27-120b.txt")

data = []

for a in f:
    ls = list(map(str, a.split()))
    ls1 = [float(ls[0]), float(ls[1]), str(ls[2])]
    data.append(ls1)


print(data)


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


r1 = [p for p in clst1 if fullmatch(r"[GJLNYSZ][0-9]II", p[2])]
r3 = [p for p in clst3 if fullmatch(r"[GJLNYSZ][0-9]II", p[2])]

rg1 = [dist(cen1, p) for p in r1]
rg3 = [dist(cen3, p) for p in r3]


b1 = sum(rg1) / len(rg1)
b2 = sum(rg3) / len(rg3)

print(b1)
print(b2)

print(int(abs(b1 * 10000)))
print(int(abs(b2 * 10000)))

# r1 = len([p for p in clst1 if fullmatch(r"G5.+", p[2])])
# r2 = len([p for p in clst2 if fullmatch(r"G5.+", p[2])])
#
# a1 = cen(clst1)[0]
# a2 = cen(clst2)[1]
#
# print(a1)
# print(a2)
#
