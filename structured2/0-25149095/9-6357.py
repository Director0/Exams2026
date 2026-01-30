f = open("9-1.txt")

cnt = 0

for s in f:
    s1 = sorted(list(map(int, s.split())))

    sp = [x for x in s1 if s1.count(x) > 1]
    snp = [x for x in s1 if s1.count(x) == 1]

    if len(sp) > 0 and len(snp) > 0 and (sum(snp) / len(snp)) < (sum(sp) / len(sp)):
        cnt += 1

print(cnt)