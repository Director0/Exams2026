f = open("27_Б.txt")

data = []

for s in f:
    ls = list(map(float, s.split()))
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
    min_dist = 10**20

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
clst4 = get_cluster(data[0])
clst5 = get_cluster(data[0])

cen1 = cen(clst1)
cen2 = cen(clst2)
cen3 = cen(clst3)
cen4 = cen(clst4)
cen5 = cen(clst5)

print(data)

print(len(clst1))
print(len(clst2))
print(len(clst3))
print(len(clst4))
print(len(clst5))

rad1 = max([dist(cen1, p) for p in clst1])
rad2 = max([dist(cen2, p) for p in clst2])
rad3 = max([dist(cen3, p) for p in clst3])
rad4 = max([dist(cen4, p) for p in clst4])
rad5 = max([dist(cen5, p) for p in clst5])

print(rad1)
print(rad2)
print(rad3)
print(rad4)
print(rad5, "\n")


print(int(max(rad1, rad2, rad3, rad4, rad5) * 10000))
print(int(min(rad1, rad2, rad3, rad4, rad5) * 10000))
