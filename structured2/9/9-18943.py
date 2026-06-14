f = open("9_18943.txt")

cnt = 0

for s in f:
    ls = list(map(int, s.split()))

    sp3 = set([x for x in ls if ls.count(x) == 3])
    sp2 = set([x for x in ls if ls.count(x) == 2])
    snp = [x for x in ls if ls.count(x) == 1]

    if len(sp3) == 1 and len(sp2) == 1 and len(snp) == 2 and sum(sp3) + sum(sp2) >= sum(snp):
        cnt += 1


print(cnt)