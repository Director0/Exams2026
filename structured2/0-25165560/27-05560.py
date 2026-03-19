f = open("27A.txt")

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


def anti(cl1, cl2):
    max_dist = -10**21

    for p1 in cl1:
        sum_dist = 0

        for p2 in cl2:
            sum_dist += dist(p1, p2)

        if sum_dist > max_dist:
            max_dist = sum_dist
            p_max = p1


    return p_max


print(len(data))

clst1 = get_cluster(data[0])
clst2 = get_cluster(data[0])

anti1 = anti(clst1, clst2)
anti2 = anti(clst2, clst1)

print(len(clst1))
print(len(clst2))

print(data)

print(anti1)
print(anti2)

print((anti1[0] + anti2[0]) / 2)
print((anti1[1] + anti2[1]) / 2)

print(int(abs((anti1[0] + anti2[0]) / 2) * 10000))
print(int(abs((anti1[1] + anti2[1]) / 2) * 10000))