f = open("27B.txt")

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
clst3 = get_cluster(data[0])
clst4 = get_cluster(data[0])

anti1 = max(anti(clst2, clst1), anti(clst3, clst1), anti(clst4, clst1))
anti2 = max(anti(clst1, clst2), anti(clst3, clst2), anti(clst4, clst2))
anti3 = max(anti(clst1, clst3), anti(clst2, clst3), anti(clst4, clst3))
anti4 = max(anti(clst1, clst4), anti(clst2, clst4), anti(clst3, clst4))

print(len(clst1))
print(len(clst2))
print(len(clst3))
print(len(clst4))

print(data)

print(anti1)
print(anti2)
print(anti3)
print(anti4)

ls = [anti1, anti2, anti3, anti4]

q1 = min([dist(p1, p2) for p1 in ls for p2 in ls if dist(p1, p2) != float(0)])
q2 = max([dist(p1, p2) for p1 in ls for p2 in ls])

print(q1)
print(q2)

print(int(q1 * 10000))
print(int(q2 * 10000))