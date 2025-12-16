f = open("9-2.txt")

num = 0


for s in f:

    num += 1
    s1 = list(map(int, s.split()))

    sp = set([b for b in s1 if s1.count(b) == 2])
    snp = [b for b in s1 if s1.count(b) == 1]

    if (len(sp) == 2 and len(snp) == 3) and ((sum(sp) / len(sp)) < max(snp)):
        print(num)