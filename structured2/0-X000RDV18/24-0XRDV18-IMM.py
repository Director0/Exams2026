s = open("24_23206.txt").read()

for x in "02468":
    s = s.replace(x, "*")

s = s.split("*")

print(s)

rs = []

for x in s:
    if x.count("S") == 35:
      rs.append(len(x))
    elif x.count("S") > 35:
        cnt = 0
        for n in range(len(x)):
            if x[n] == "S":
                cnt += 1

            if cnt == 36:
                rs.append(n)
                break


print(max(rs) + 1)