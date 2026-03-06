f = open("27_B.txt")

data = []

for a in f:
    ls = list(map(float, a.split()))

    data.append(ls)


def dist(p1, p2):
    return (((p1[0] - p2[0])**2) + ((p1[1] - p2[1])**2)) ** 0.5


def get_cluster(p0):
    clst = [p for p in data if dist(p0, p) <= 5.5]

    for a in clst:
        data.remove(a)


    clst1 = [get_cluster(p) for p in clst]
    clst += sum(clst1, [])

    return clst


def cpi(clst):
    x = [a[0] for a in clst]
    y = [a[1] for a in clst]

    xs = sum(x) / len(x)
    ys = sum(y) / len(y)

    si1 = sum([(x0 - xs) * (y0 - ys) for x0, y0 in clst])

    sxi2 = sum([(x0 - xs)**2 for x0 in x])
    syi2 = sum([(y0 - ys)**2 for y0 in y])

    return (si1) / ((sxi2 * syi2) ** 0.5)


print(len(data))

clst1 = get_cluster(data[0])
clst2 = get_cluster(data[0])
clst3 = get_cluster(data[0])
clst4 = get_cluster(data[0])
clst5 = get_cluster(data[0])


cp1 = cpi(clst1)
cp2 = cpi(clst2)
cp3 = cpi(clst3)
cp4 = cpi(clst4)
cp5 = cpi(clst5)

print(len(clst1))
print(len(clst2))
print(len(clst3))
print(len(clst4))
print(len(clst5))
print(data)

print(cp1)
print(cp2)
print(cp3)
print(cp4)
print(cp5)

print(len(clst1) + len(clst2) + len(clst3))
print(int(((cp1 + cp2 + cp3) / 3) * 100000))