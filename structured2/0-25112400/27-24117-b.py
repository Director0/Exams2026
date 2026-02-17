f = open("27B_24117.txt")

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
clst3 = get_cluster(data[0])

acen1 = anticen(clst1)
acen2 = anticen(clst2)
acen3 = anticen(clst3)

print(len(clst1))
print(len(clst2))
print(len(clst3))
print(data)

print(acen1)
print(acen2)
print(acen3)

print(dist(acen2, acen3))

d1 = max([dist(acen1, p) for p in clst1])
d2 = max([dist(acen2, p) for p in clst2])
d3 = max([dist(acen3, p) for p in clst3])

print(max(d1, d2, d3))

print(int(abs(dist(acen2, acen3) * 10000)))
print(int(abs(max(d1, d2, d3) * 10000)))
