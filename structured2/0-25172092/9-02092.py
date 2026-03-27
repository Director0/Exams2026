f = open("9_02092.txt")

cnt = 0

for s in f:
    ls = list(map(int, s.split()))

    sp2 = [x for x in ls if x % 2 == 0]
    spn = [x for x in ls if x % 2 != 0]

    sp = [x for x in ls if ls.count(x) > 1]

    if len(sp) == 0 and len(sp2) > len(spn) and sum(sp2) < sum(spn):
        cnt += 1


print(cnt)