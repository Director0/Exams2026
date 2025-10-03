f = open("27.13.B_19567.txt")

data = []

for s in f:
    lst = list(map(float, s.split()))
    data.append(lst)

def dist(p1, p2):
    return (((p1[0] - p2[0])**2) + ((p1[1] - p2[1])**2)) ** 0.5

def get_cluster(p0):
    clst = [p for p in data if dist(p0, p) <= 0.5]

    for a in clst:
        data.remove(a)

    clst1 = [get_cluster(p) for p in clst]
    clst += sum(clst1, [])

    return clst




def centroid(clst):
    min_dist = 10**20

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
clst6 = get_cluster(data[0])


cen1 = centroid(clst1)
cen2 = centroid(clst2)
cen3 = centroid(clst3)
cen4 = centroid(clst4)
cen5 = centroid(clst5)
cen6 = centroid(clst6)


print(len(clst1), len(clst2), len(clst3), len(clst4), len(clst5), len(clst6), sep="\n")


print(cen1, cen2, cen3, cen4)
print(int(abs(((cen1[0] + cen2[0] + cen3[0] + cen4[0] + cen5[0] + cen6[0]) / 6) * 10000)), int(abs(((cen1[1] + cen2[1] + cen3[1] + cen4[1] + cen5[1] + cen6[1]) / 6) * 10000))) #abs((cen1[1] + cen2[1] + cen3[1] + cen4[1] + cen5[1] + cen6[1]) * 10000 // 4))