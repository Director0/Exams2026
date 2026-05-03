f = open("9_1_2.txt")

cnt = 0

for s in f:
    ls = sorted(list(map(int, s.split())))
    ls1 = sorted([x for x in ls if ls.count(x) == 1])

    if ((ls.count(ls[0]) == 2 and len(set(ls)) == 7) or (ls.count(ls[0]) == 3 and len(set(ls)) == 6)) and ((ls1[0]**2 + ls1[-1]**2) <= sum(ls1[1:-1])**2):
        cnt += 1


print(cnt)