from re import *

f = open("27_B_29357.txt")

data = [[float(a), float(b), str(c)] for a, b, c in list(map(str, s.split()) for s in f)]


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


rg1 = [len([p for p in clstx if fullmatch(r"K[0-9]III", p[2])]) for clstx in [clst1, clst2, clst3]]
rgx1 = [dist(p1, p2) for p1 in clst1 if fullmatch(r"G[0-9]V", p1[2]) for p2 in clst1 if fullmatch(r"G[0-9]V", p2[2]) if dist(p1, p2) > 0 ]
rgx2 = [dist(p1, p2) for p1 in clst2 if fullmatch(r"G[0-9]V", p1[2]) for p2 in clst2 if fullmatch(r"G[0-9]V", p2[2]) if dist(p1, p2) > 0 ]
rgx3 = [dist(p1, p2) for p1 in clst3 if fullmatch(r"G[0-9]V", p1[2]) for p2 in clst3 if fullmatch(r"G[0-9]V", p2[2]) if dist(p1, p2) > 0 ]

print(rg1)


b1 = dist(cen1, cen3)
b2 = max(rgx1 + rgx2 + rgx3)

print(b1)
print(b2)

print(int(b1 * 10000))
print(int(b2 * 10000))
