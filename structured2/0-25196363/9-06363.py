f = open("9_06363.txt")

cnt = 0

for s in f:
    ls = list(map(int, s.split()))

    sp = set([x for x in ls if ls.count(x) == 3])
    snp = [x for x in ls if ls.count(x) == 1]

    if len(sp) == 1 and len(snp) == 3 and sum(snp) / len(snp) <= list(sp)[0]*3:
        cnt += 1


print(cnt)