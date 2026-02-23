f = open("26_8380.txt")

# 10 500

line = [0] * 10

lns = []
lns.append(line)



for s in f:
    s1 = list(map(int, s.split()))

    flag = False

    for il in range(len(lns)):
        for i in range(len(lns[il])):

            if lns[il][i] < s1[0]:
                lns[il][i] = s1[1]
                flag = True
                break

        if flag == True:
            break


    if flag == False:
        lns.append([0] * 10)

        lns[-1][0] = s1[1]


print(lns)
print(len(lns))