from re import *

f = open("27_A_29081.txt")

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

cen1 = cen(clst1)
cen2 = cen(clst2)


print(len(clst1))
print(len(clst2))

print(data)

print(cen1)
print(cen2)

kv1 = [p for p in clst1 if fullmatch(r"[GJLNYSZ][0-9]VII", p[2])]
kv2 = [p for p in clst2 if fullmatch(r"[GJLNYSZ][0-9]VII", p[2])]

k1 = min(dist(cen1, p) for p in kv1)
k2 = min(dist(cen2, p) for p in kv2)

k11 = max(dist(cen1, p) for p in kv1)
k12 = max(dist(cen2, p) for p in kv2)


a1 = min(k1, k2)
a2 = max(k11, k12)

print(a1)
print(a2)

print(int(a1 * 10000))
print(int(a2 * 10000))