f = open("27_B.txt")

data = []

for s in f:
    lst = list(map(float, s.split()))
    data.append(lst)

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

cen1 = cen(clst1)
cen2 = cen(clst2)
cen3 = cen(clst3)

acen1 = anticen(clst1)
acen2 = anticen(clst2)
acen3 = anticen(clst3)

print(data)

print(len(clst1))
print(len(clst2))
print(len(clst3))


print(acen1)
print(acen2)
print(acen3)

print(int(acen1[0] * 10000))
print(int(acen2[1] * 10000))