f = open("27_A.txt")

data = []

for a in f:
    ls = list(map(float, a.split()))
    data.append(ls)


def dist(p1, p2):
    return (((p1[0] - p2[0])**2) + ((p1[1] - p2[1])**2)) ** 0.5


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


def cdi(cenx, clst):
    sum_dist = 0

    for p1 in clst:
        sum_dist += dist(cenx, p1)

    return sum_dist


print(len(data))

clst1 = get_cluster(data[0])
clst2 = get_cluster(data[0])

cen1 = cen(clst1)
cen2 = cen(clst2)

print(len(clst1))
print(len(clst2))

s1 = max(cdi(cen1, clst2), cdi(cen2, clst1))
d1 = dist(cen1, cen2)

print(s1)
print(d1)

print(int(s1 * 100))
print(int(d1 * 100))