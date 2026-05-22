f = open("9_18364.txt")


cnt = 0

for s in f:
    ls = list(map(int, s.split()))

    sp = [x for x in ls if ls.count(x) > 1]
    sxc = 1
    snp = [x for x in ls if ls.count(x) == 1]

    for x in sp:
        sxc *= x

    if len(sp) > 0 and 3 * sum(snp) <= sxc:
        cnt += 1


print(cnt)