f = open("9_00284.txt")

cnt = 0

for s in f:
    ls = list(map(int, s.split()))

    sp = set([x for x in ls if ls.count(x) == 2])
    snp = [x for x in ls if ls.count(x) == 1]

    if (len(sp) == 1 and len(snp) == 3) or sum([x for x in ls if x % 2 != 0]) > sum([x for x in ls if x % 2 == 0]):
        cnt += 1


print(cnt)