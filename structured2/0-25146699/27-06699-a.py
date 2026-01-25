f = open("27_A.txt")

pa = [1, 1]
rsa = 2

pb = [20, 20]
rsb = 3


data = []

for s in f:
    lst = list(map(float, s.split()))
    data.append(lst)

def dist(p1, p2):
    return (((p1[0] - p2[0])**2) + ((p1[1] - p2[1])**2)) ** 0.5

def get_cluster(p0, rs):
    clst = [dist(p0, p) for p in data if rs < dist(p0, p) < 3 * rs]

    return clst


# print(data)
# print(len(data))

clst1 = get_cluster(pa, rsa)
clst2 = get_cluster(pb, rsb)

# print(len(data), data, sep="\n")

print(clst1)
print(clst2)

print(len(clst1))
print(len(clst2))

print(sum(clst1) / len(clst1))
print(sum(clst2) / len(clst2))

print((sum(clst1) / len(clst1)) * 1000)
print((sum(clst2) / len(clst2)) * 1000)
# print(cen1, cen2)
# print(int(abs(((cen1[0] + cen2[0]) / 2) * 10000)), int(abs(((cen1[1] + cen2[1]) / 2) * 10000)))