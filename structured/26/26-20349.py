f = open("26-20349.txt")

data = []


for a in f:
    ls = list(map(int, a.split()))
    data.append(ls)

data.sort()
l1 = len(data)

ray1 = [n for n in data if 0 not in n]
ray2 = [n for n in data if n.count(0) > 5]

for i in range(len(ray1)):
    ray1[i].insert(0, sum(ray1[i][1:]) / 10)

ray1.sort(key=lambda x:x[1])
ray1.sort(reverse=True, key = lambda x:x[0])
rayx = ray1[:1990]
print(rayx[-1])

print(ray2[0])

# 8658 495