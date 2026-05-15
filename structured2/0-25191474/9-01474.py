f = open("9_01474.txt")

cnt = 0

for s in f:
    ls = list(map(int, s.split()))

    ls1 = set([x for x in ls if ls.count(x) == 3])
    ls2 = [x for x in ls if ls.count(x) == 1]

    if len(ls1) == 1 and len(ls2) == 4 and sum(ls2) / len(ls2) <= list(ls1)[0]:
        cnt += 1


print(cnt)