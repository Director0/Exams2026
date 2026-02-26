f = open("27A_25755.txt")

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
    min_dist = 10**10

    for p1 in clst:
        sum_dist = 0

        for p2 in clst:
            sum_dist += dist(p1, p2)

        if sum_dist < min_dist:
            min_dist = sum_dist
            p_min = p1


    return p_min


def borderdot(cl1, cl2):
    min_dist = 100

    for p1 in cl1:
        for p2 in cl2:
            d = dist(p1, p2)

        if d < min_dist:
            min_dist = d
            bdrs = [p1, p2]


    return bdrs



print(len(data))

clst1 = get_cluster(data[0])
clst2 = get_cluster(data[0])
clst3 = get_cluster(data[0])

# cen1 = cen(clst1)
# cen2 = cen(clst2)
# cen3 = cen(clst3)

b12 = borderdot(clst1, clst2)
b13 = borderdot(clst1, clst3)
b23 = borderdot(clst2, clst3)

print(len(clst1))
print(len(clst2))
print(len(clst3))
print(data)

print(b12)
print(b13)
print(b23)

print(((b12[0][0] + b12[1][0] + b13[0][0] + b13[1][0] + b23[0][0] + b23[1][0]) / 6))
print(int(abs(((b12[0][1] + b12[1][1] + b13[0][1] + b13[1][1] + b23[0][1] + b23[1][1]) / 6) * 10000)))