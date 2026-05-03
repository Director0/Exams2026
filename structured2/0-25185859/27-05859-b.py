f = open("27B.txt")

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
clst3 = get_cluster(data[0])


diam1 = diam(clst1)
diam2 = diam(clst2)
diam3 = diam(clst3)

print(len(clst1))
print(len(clst2))
print(len(clst3))

print(data)
print(diam1)
print(diam2)
print(diam3)


q1 = diam2[0]
rg0 = [diam1[1], diam1[2], diam2[1], diam2[2], diam3[1], diam3[2]]
q2 = dist(min(rg0, key=lambda x:x[1]), max(rg0, key=lambda x:x[1]))

print(q1)
print(q2)

print(int(q1 * 10000))
print(int(q2 * 10000))