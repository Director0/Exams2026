f = open("9_08035.txt")

cnt = 0

for s in f:
    ls = sorted(list(map(int, s.split())))

    if (ls[0] + ls[-1]) / 2 <= ls[1]:
        cnt += 1


print(cnt)

