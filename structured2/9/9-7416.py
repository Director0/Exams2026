f = open("9_7416.txt")

for s in f:
    ls = list(map(int, s.split()))

    sp = set([x for x in ls if ls.count(x) >= 2])
    snp = set(ls)

    if len(snp) == 2:
        a,b = snp


    if len(snp) == 2 and len(sp) == 2 and (2*a + 2*b) < (sum(ls) - (2*a + 2*b)):
        print(sum(ls))