from re import *

f = open("27_A_28766.txt")

data = []

for a in f:
    a1 = list(map(str, a.split()))
    ls = [float(a1[0]), float(a1[1]), str(a1[2])]
    data.append(ls)



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

cen1 = cen(clst1)
cen2 = cen(clst2)

rg = [p for p in clst2 if fullmatch(r"Y[1-9]III", p[2])]
rg1 = [p for p in clst1 if fullmatch(r"Y[1-9]III", p[2])]
a1 = dist(cen2, rg[0])
a2 = max(dist(cen2, r) for r in rg1)

print(len(clst1))
print(len(clst2))
print(data)
print(rg)
print(rg1)
print(int(a1 * 10000))
print(int(a2 * 10000))


