f = open("27B_22623.txt")

data = []
sqr = 4 * 4

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
    min_dist = 10**22

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

pro1 = len(clst1) / sqr
pro2 = len(clst2) / sqr
pro3 = len(clst3) / sqr
pro4 = len(clst4) / sqr
pro5 = len(clst5) / sqr

print(len(clst1))
print(len(clst2))
print(len(clst3))
print(len(clst4))
print(len(clst5), "\n")

print(cen1)
print(cen2)
print(cen3)
print(cen4)
print(cen5, "\n")

print(pro1)
print(pro2)
print(pro3)
print(pro4)
print(pro5, "\n")

ps = (pro1 + pro2 + pro3 + pro4 + pro5) / 5
sp = dist(cen1, cen5)

print(ps)
print(sp, "\n")

print(int(ps * 1000))
print(int(sp * 1000))