f = open("9_58476-s.txt")

cnt = 0

for s in f:
    ls = sorted(list(map(int, s.split())))

    sp = set([x for x in ls if ls.count(x) > 1])
    snp = [x for x in ls if ls.count(x) == 1]

    if len(sp) > 0 and max(ls) in snp and max(ls) > (sum(ls[:-1]) / len(ls[:-1])) * 3:
        cnt += 1


print(cnt)