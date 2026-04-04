f = open("27A.txt")

data = []

for a in f:
    ls = list(map(float, a.split()))

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


def anticen(clst):
    max_dist = -10**21

    for p1 in clst:
        sum_dist = 0

        for p2 in clst:
            sum_dist += dist(p1, p2)

        if sum_dist > max_dist:
            max_dist = sum_dist
            p_max = p1


    return p_max


print(len(data))

clst1 = get_cluster(data[0])
clst2 = get_cluster(data[0])

acen1 = anticen(clst1)
acen2 = anticen(clst2)

print(len(clst1))
print(len(clst2))

print(data)

print(acen1)
print(acen2)

px = acen1[0] + acen1[1]
py = acen2[0] + acen2[1]

print(px)
print(py)

print(abs(int(px * 10000)))
print(abs(int(py * 10000)))