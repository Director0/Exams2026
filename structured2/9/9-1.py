f = open("9-1.txt")

num = 0


for s in f:

    num += 1
    s1 = sorted(list(map(int, s.split())))

    sp = set([b for b in s1 if s1.count(b) == 3])
    snp = [b for b in s1 if s1.count(b) == 1]

    if (len(sp) == 1 and len(snp) == 4) and ((sum(s1[5:7]) > sum(s1[0:5]))):
        print(num)


# num: 1433