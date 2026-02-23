f = open("27B_2_20207.txt")

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

def medx(clst):
    max_dist = -10**21

    for p in clst:
        sum_dist = 0

        sum1 = [x for x in clst if x[0] > p[0]]
        sum2 = [x for x in clst if x[0] < p[0]]

        if len(sum1) == len(sum2):
            return p


def medy(clst):
    max_dist = -10**21

    for p in clst:
        sum_dist = 0

        sum1 = [x for x in clst if x[1] > p[1]]
        sum2 = [x for x in clst if x[1] < p[1]]

        if len(sum1) == len(sum2) and len(sum1) == (len(clst) - 1) // 2:
            return p



print(len(data))

clst1 = get_cluster(data[0])
clst2 = get_cluster(data[0])
clst3 = get_cluster(data[0])

med1x = medx(clst1)
med2x = medx(clst2)
med3x = medx(clst3)

med1y = medy(clst1)
med2y = medy(clst2)
med3y = medy(clst3)

print(len(clst1))
print(len(clst2))
print(len(clst3))
print(data)

print(med1x)
print(med2x)
print(med3x)

print(med1y)
print(med2y)
print(med3y)

print(int((med1x[0] + med2x[0] + med3x[0])/3 * 10000))
print(int((med1y[1] + med2y[1] + med3y[1])/3 * 10000))