f = open("27_A.txt")

pd1 = [1, 1]
rd1 = 2

pd2 = [20, 20]
rd2 = 3


data = []

for s in f:
    lst = list(map(float, s.split()))
    data.append(lst)

def dist(p1, p2):
    return (((p1[0] - p2[0])**2) + ((p1[1] - p2[1])**2)) ** 0.5

def get_cluster(p0, rd):
    clst = [dist(p0, p) for p in data if rd <= dist(p0, p) <= 3 * rd]

    return clst


print(len(data))

clst1 = get_cluster(pd1, rd1)
clst2 = get_cluster(pd2, rd2)

print(clst1)
print(clst2)

print(len(clst1))
print(len(clst2))

q1 = sum(clst1) / len(clst1)
q2 = sum(clst2) / len(clst2)

print(int(q1 * 1000), int(q2 * 1000))
