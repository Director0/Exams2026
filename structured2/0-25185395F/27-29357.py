from re import *

f = open("27_A_29357.txt")

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

cen1 = cen(clst1)
cen2 = cen(clst2)

print(len(clst1))
print(len(clst2))

print(data)


rg1 = [p + [dist(p, cen1)] for p in clst1 if fullmatch(r"M[0-9]III", p[2])]
print(rg1)

a = min(rg1, key=lambda x:x[3])

print(a[0])
print(a[1])

print(int(abs(a[0] * 10000)))
print(int(abs(a[1] * 10000)))