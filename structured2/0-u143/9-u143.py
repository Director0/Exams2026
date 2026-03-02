f = open("9_u143.txt")

cnt = 0

for s in f:
    ls = list(map(int, s.split()))

    sp = set([x for x in ls if ls.count(x) > 1])
    snp = [x for x in ls if ls.count(x) == 1]

    if (len(snp) == 4) and (sum(sp) < sum(snp)):
        cnt += 1


print(cnt)