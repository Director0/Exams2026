from re import *
from itertools import *

f = open("27_B_29081.txt")

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


# cen1 = cen(clst1)
# cen2 = cen(clst2)
# cen3 = cen(clst3)


print(len(clst1))
print(len(clst2))
print(len(clst3))

print(data)





kv1 = [p for p in clst1 if fullmatch(r"[GJLNYSZ][89].+", p[2])]
kv2 = [p for p in clst2 if fullmatch(r"[GJLNYSZ][89].+", p[2])]
kv3 = [p for p in clst3 if fullmatch(r"[GJLNYSZ][89].+", p[2])]

b12 = min(dist(p1, p2) for p1 in kv1 for p2 in kv2)
b23 = min(dist(p2, p3) for p2 in kv2 for p3 in kv3)
b13 = min(dist(p1, p3) for p1 in kv1 for p3 in kv3)

k1 = [dist(p1, p2) for p1, p2 in combinations(kv1, r=2)]
k2 = [dist(p1, p2) for p1, p2 in combinations(kv2, r=2)]
k3 = [dist(p1, p2) for p1, p2 in combinations(kv3, r=2)]

rk = k1 + k2 + k3


b1 = min(b12, b23, b13)
b2 = sum(rk) / len(rk)


print(b1)
print(b2)

print(int(b1 * 10000))
print(int(b2 * 10000))