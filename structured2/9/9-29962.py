f = open("9_29962.txt")

num = 0

for s in f:
    num += 1
    ls = list(map(int, s.split()))

    sp = set([x for x in ls if ls.count(x) == 3])
    snp = [x for x in ls if ls.count(x) == 1]

    if len(sp) == 1 and len(snp) == 4 and sum(snp) / len(snp) > list(sp)[0]:
        print(num, ls)


