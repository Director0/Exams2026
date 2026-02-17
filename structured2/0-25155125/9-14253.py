from math import sqrt

f = open("9_14253.txt")

cnt = 0

for s in f:
    ls = list(map(int, s.split()))

    sp = set([x for x in ls if ls.count(x) == 2])
    snp = [x for x in ls if ls.count(x) == 1]

    if (len(sp) == 3 and len(snp) == 1) or (((sum(ls) / len(ls)) ** 0.5) % 1 == 0):
        cnt += 1


print(cnt)