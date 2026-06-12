f = open("9_09540.txt")


cnt = 0

for s in f:
    ls = list(map(int, s.split()))

    sp = [x for x in ls if ls.count(x) >= 2]
    snp = [x for x in ls if ls.count(x) == 1]

    if min(ls) not in sp and len(snp) != len(ls) and min(ls) + max(ls) < sum(sp):
        cnt += 1


print(cnt)