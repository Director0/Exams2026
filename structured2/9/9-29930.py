f = open("9_29930.txt")

cnt = 0

for s in f:
    ls = list(map(int, s.split()))
    lx = sorted(ls)

    if len(ls) == len(set(ls)) and ls == sorted(ls) and lx[0] + lx[-1] <= sum(lx[1:-1]):
        cnt += 1


print(cnt)