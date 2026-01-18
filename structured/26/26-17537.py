# 9990 99938 6660

f = open("26_17537.txt")

data = []
rs = []
r1 = []

for s in f:
    rm = list(map(int, s.split()))
    data.append(rm)

data.sort()
print(data)

for i in range(len(data)):
    rs.append(data[i][0])

print(rs)

for i in rs:
    r1.append([i, rs.count(i)])

print(r1)
r1.sort(key=lambda x:x[1])

r_res = r1[-1][0] - 1

print(r_res)

# for r in range(7):
#     for m in range(8):
#         if [r, m] in data:
#             rs.append("1")