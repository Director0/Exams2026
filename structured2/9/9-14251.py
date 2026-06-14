f = open("9_14251.txt")

num = 0

for s in f:
    num += 1
    ls = list(map(int, s.split()))

    sp = set([x for x in ls if ls.count(x) == 2])
    snp = [x for x in ls if ls.count(x) == 1]

    if len(sp) == 2 and len(snp) == 3 and list(sp)[0]*2 + list(sp)[1]*2 <= sum([x for x in ls if x % 2 != 0]):
        print(num, ls, sum(ls))