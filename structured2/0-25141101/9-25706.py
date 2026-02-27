f = open("9_25706.txt")

cnt = 0

for s in f:
    ls = list(map(int, s.split()))

    sp = [x for x in ls if x % 3 == 0]

    if (sum(ls) % min(ls) == 0) or (len(sp) > 3):
        cnt += 1


print(cnt)