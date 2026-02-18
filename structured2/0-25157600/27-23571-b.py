f = open("27_B_23571.txt")

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
    min_dist = 10 ** 20

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

d1 = min([dist(p1, p2) for p1 in clst1 for p2 in clst2])
d2 = min([dist(p1, p3) for p1 in clst1 for p3 in clst3])
d3 = min([dist(p2, p3) for p2 in clst2 for p3 in clst3])

d11 = max([dist(p1, p2) for p1 in clst1 for p2 in clst2])
d12 = max([dist(p1, p3) for p1 in clst1 for p3 in clst3])
d13 = max([dist(p2, p3) for p2 in clst2 for p3 in clst3])

print(len(clst1))
print(len(clst2))
print(len(clst3))

print(data)

print(int(min(d1, d2, d3) * 10000))
print(int(max(d11, d12, d13) * 10000))