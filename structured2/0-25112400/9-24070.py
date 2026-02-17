f = open("9_24070.txt")

cnt = 0

for s in f:
    ls = sorted(list(map(int, s.split())))

    snp = [x for x in ls if ls.count(x) == 1]

    if (len(snp) == len(ls)) and ((ls[0] + ls[4]) <= (ls[1] + ls[2] + ls[3])):
        cnt += 1


print(cnt)