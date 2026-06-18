s = open("24_9753.txt").read()

pos = []

for i in range(len(s)):
    if s[i] == "Y":
        pos.append(i)



rs = []

for i in range(len(pos) - 150):
    rs.append(pos[i + 150] - pos[i])


print(max(rs))