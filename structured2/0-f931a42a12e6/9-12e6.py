f = open("9_12e6.txt")

cnt = 0

for s in f:
    ls = sorted(list(map(int, s.split())))

    if (len([x for x in ls if x < 0]) == 0 or len([x for x in ls if x > 0])) == 0: continue

    if (len([x for x in ls if x < 0]) > len([x for x in ls if x > 0])) and (abs(ls[0]) > ls[-1]):
        cnt += 1


print(cnt)