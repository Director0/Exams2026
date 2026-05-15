f = open("9_4635.txt")

cnt = 0

for s in f:
    ls = sorted(list(map(int, s.split())))

    sp = [x for x in ls if ls.count(x) > 1]

    if ls.count(ls[-1]) == 1 and 2 * ls[0]**2 > (ls[1] * ls[2]) and len(sp) > 0:
        cnt += 1


print(cnt)