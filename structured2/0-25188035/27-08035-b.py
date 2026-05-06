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

cen1 = cen(clst1)
cen2 = cen(clst2)
cen3 = cen(clst3)

print(len(clst1))
print(len(clst2))
print(len(clst3))

print(data)

print(cen1)
print(cen2)
print(cen3)


rq3 = [dist(cen3, p) for p in clst3 if p != cen3]
rq2 = [dist(cen2, p) for p in clst2 if p != cen2]

q1 = sum(rq3) / len(rq3)
q2 = sum(rq2) / len(rq2)

print(q1)
print(q2)

print(abs(int(q1 * 10000)))
print(abs(int(q2 * 10000)))



