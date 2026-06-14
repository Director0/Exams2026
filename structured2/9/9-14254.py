f = open("9_14254.txt")

cnt = 0

for s in f:
    ls = sorted(list(map(int, s.split())))

    sp = [x for x in ls if ls.count(x) > 1]
    snp = [x for x in ls if ls.count(x) == 1]

    if ls[0] * ls[-1] < sum(ls[1:-1]) * 3 and sum(snp) <= sum(sp):
        cnt += 1


print(cnt)
