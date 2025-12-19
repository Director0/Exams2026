f = open("9_24362.txt")

num = 0


for s in f:

    num += 1
    s1 = sorted(list(map(int, s.split())))

    sp = set([b for b in s1 if s1.count(b) == 2])
    snp = [b for b in s1 if s1.count(b) == 1]

    if (len(sp) == 2 and len(snp) == 2) and max(s1) not in sp and min(s1) not in sp:
        print(num)
