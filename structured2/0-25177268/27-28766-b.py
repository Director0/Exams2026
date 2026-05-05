from re import *

f = open("27_B_28766.txt")

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
clst3 = get_cluster(data[0])

cen1 = cen(clst1)
cen2 = cen(clst2)
cen3 = cen(clst3)

rg1 = [p for p in clst1 if fullmatch(r"Z[1-9]I", p[2])]
rg2 = [p for p in clst2 if fullmatch(r"Z[1-9]I", p[2])]
rg3 = [p for p in clst3 if fullmatch(r"Z[1-9]I", p[2])]


b11 = min([dist(p1, p2) for p1 in clst1 for p2 in clst1 if dist(p1, p2) > 0])
b13 = min([dist(p1, p2) for p1 in clst3 for p2 in clst3 if dist(p1, p2) > 0])

b1 = min(b11, b13)

print(b1)

print(len(clst1))
print(len(clst2))
print(data)
print(rg1)
print(rg2)
print(rg3)
print(int(b1 * 10000))
# print(int(a2 * 10000))


