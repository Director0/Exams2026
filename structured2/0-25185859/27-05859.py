f = open("27A.txt")

data = [list(map(float, a.split())) for a in f]


def dist(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5


def get_cluster(p0):
    clst = [p for p in data if dist(p0, p) <= 1]

    for a in clst:
        data.remove(a)

    clst1 = [get_cluster(p) for p in clst]
    clst += sum(clst1, [])

    return clst


def diam(clst):
    max_dist = -10**21

    for p1 in clst:
        for p2 in clst:
            if dist(p1, p2) > max_dist:
                max_dist = dist(p1, p2)
                pb1 = p1
                pb2 = p2

    return [max_dist, pb1, pb2]


print(len(data))

clst1 = get_cluster(data[0])
clst2 = get_cluster(data[0])


diam1 = diam(clst1)
diam2 = diam(clst2)

print(len(clst1))
print(len(clst2))

print(data)
print(diam1)
print(diam2)

px = min(diam1[1][0] + diam1[2][0], diam2[1][0] + diam2[2][0])
py = max(diam1[1][1] + diam1[2][1], diam2[1][1] + diam2[2][1])

print(px)
print(py)

print(abs(int(px * 10000)))
print(abs(int(py * 10000)))
# q1 = diam1
# q2 = max(dist(diam1[1], diam2[1]), dist(diam1[1], diam2[2]), dist(diam1[2], diam2[1]), dist(diam1[2], diam2[2]))
#
# print(q1)
# print(q2)
#
# print()