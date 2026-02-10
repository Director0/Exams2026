f = open("9-07520.txt")

cnt = 0

for s in f:
    lst = list(map(int, s.split()))

    sp = set([x for x in lst if lst.count(x) == 2])
    snp = [x for x in lst if lst.count(x) == 1]

    if len(sp) == 1 and len(snp) == 3:
        cnt += 1


print(cnt)