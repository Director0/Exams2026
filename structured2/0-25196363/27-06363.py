f = open("27.19.A.txt")

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


def anti(clst):
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

ant1 = anti(clst1)
ant2 = anti(clst2)
ant3 = anti(clst3)


print(len(clst1))
print(len(clst2))
print(len(clst3))

print(data)

print(ant1)
print(ant2)
print(ant3)

tx = (ant1[0] + ant2[0] + ant3[0]) / 3
ty = (ant1[1] + ant2[1] + ant3[1]) / 3

print(tx)
print(ty)

print(int(abs(tx * 10000)))
print(int(abs(ty * 10000)))