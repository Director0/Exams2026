f = open("26.txt")

spc = [0] * 20
rs = []
rs1 = []

print(spc)

for s in f:
    ls = list(map(int, s.split()))
    for i in range(len(spc)):
        if spc[i] <= ls[0]:
            spc[i] = ls[1]
            rs1.append(ls[0])
        else:
            rs.append(ls[1])


print(len(rs1))