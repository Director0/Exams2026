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


print(len(clst1))
print(len(clst2))
print(len(clst3))
print(data)


b1 = min([dist(p1, p2) for p1 in clst1 for p2 in clst1 if p1 != p2 and fullmatch(r"Z[0-9]I", p1[2]) and fullmatch(r"Z[0-9]I", p2[2])] + [dist(p1, p2) for p1 in clst2 for p2 in clst2 if p1 != p2 and fullmatch(r"Z[0-9]I", p1[2]) and fullmatch(r"Z[0-9]I", p2[2])])
b2 = dist(cen1, cen2)

print(b1)
print(b2)

print(int(abs(b1 * 10000)))
print(int(abs(b2 * 10000)))
