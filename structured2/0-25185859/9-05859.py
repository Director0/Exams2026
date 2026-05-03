f = open("9_05859.txt")

cnt = 0

for s in f:
    ls = sorted(list(map(int, s.split())))

    if len(set([x for x in ls if ls.count(x) == 2])) == 2 and len([x for x in ls if ls.count(x) == 1]) == 3 and (ls[0] * ls[1]) > sum(ls[2:]):
        cnt += 1


print(cnt)