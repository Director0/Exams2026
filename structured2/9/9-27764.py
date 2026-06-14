f = open("9_27764.txt")

cnt = 0

for s in f:
    ls = sorted(list(map(int, s.split())))

    if len(ls) == len(set(ls)) and 2 * (ls[0] + ls[-1]) == sum(ls[1:-1]):
        cnt += 1


print(cnt)