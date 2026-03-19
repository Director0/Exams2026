f = open("27_A.txt")

data = []

for a in data:
    ls = list(map(float, a.split()))

    ls.append()

def dist(p1, p2):
    return (((p1[0] - p2[0])**2) + ((p1[1] - p2[1])**2)) ** 0.5


def get_cluster(p0):
    clst = [p for p in data if dist(p0, p) <= 1]

    for a in clst:
        data.remove(a)