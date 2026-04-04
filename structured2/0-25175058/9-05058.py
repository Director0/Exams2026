f = open("9_05058.txt")

cnt = 0

for s in f:
    ls = list(map(int, s.split()))

    sp = [x for x in ls if x % 2 == 0]
    snp = [x for x in ls if x % 2 != 0]

    if sum(snp) > sum(sp):
        cnt += 1


print(cnt)