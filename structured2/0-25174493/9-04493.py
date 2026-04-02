f = open("9_04493.txt")

cnt = 0

for s in f:
    ls = list(map(int, s.split()))

    if len([x for x in ls if str(x)[-1] == "3"]) == 3 and sum([x for x in ls if x > 0])**2 < sum([x for x in ls if x < 0])**2:
        cnt += 1


print(cnt)