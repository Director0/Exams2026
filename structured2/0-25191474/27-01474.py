f = open("27_A.txt")

n = f.readline()

pa = [1, 1]
rsa = 2

pb = [20, 20]
rsb = 3


data = [list(map(float, a.split())) for a in f]


def dist(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5


def get_cluster(p0, rs):
    clst = [dist(p0, p) for p in data if rs <= dist(p0, p) <= 3 * rs]

    return clst

rg1 = get_cluster(pa, rsa)
rg2 = get_cluster(pb, rsb)

a1 = sum(rg1) / len(rg1)
a2 = sum(rg2) / len(rg2)

print(a1)
print(a2)

print(int(a1 * 1000))
print(int(a2 * 1000))
