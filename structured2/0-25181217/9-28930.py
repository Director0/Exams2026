f = open("9_28930.txt")

cnt = 0

for s in f:
    ls = list(map(int, s.split()))
    ls1 = sorted(ls)

    if len([x for x in ls if ls.count(x) == 1]) == len(ls) and ls == ls1 and (ls1[0] + ls1[-1]) <= sum(ls) - max(ls) - min(ls):
        cnt += 1


print(cnt)