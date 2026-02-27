f = open("9_a422.txt")

cnt = 0

for s in f:
    ls = list(map(int, s.split()))

    sv = 1
    sc = [x for x in ls if x % 2 == 0]
    snc = [x for x in ls if x % 2 != 0]

    for x in sc:
        sv *= x

    if len(sc) >= 2 and len(snc) >= 2 and sum(snc) * 3 > sv:
        cnt += 1


print(cnt)