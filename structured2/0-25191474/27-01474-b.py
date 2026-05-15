f = open("27_B.txt")

n = f.readline()

pa = [1.5, 1.7]
rsa = 3

pb = [-25.2, -40.1]
rsb = 4

pc = [30.7, 44.4]
rsc = 5


data = [list(map(float, a.split())) for a in f]


def dist(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5


def get_cluster(p0, rs):
    clst = [dist(p0, p) - rs for p in data if rs <= dist(p0, p) <= 3 * rs]

    return clst

rg1 = get_cluster(pa, rsa)
rg2 = get_cluster(pb, rsb)
rg3 = get_cluster(pc, rsc)

a1 = sum(rg1) / len(rg1)
a2 = sum(rg2) / len(rg2)
a3 = sum(rg3) / len(rg3)

print(a1)
print(a2)
print(a3)

print(int(a1 * 1000))
print(int(a2 * 1000))
print(int(a3 * 1000))
