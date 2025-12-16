f = open("9-3.txt")

num = 0
gcnt = 0


for s in f:

    num += 1
    s1 = list(map(int, s.split()))

    sp = set([b for b in s1 if s1.count(b) == 2])
    snp = [b for b in s1 if s1.count(b) == 1]

    if (len(sp) == 3 and len(snp) == 1) and (snp[0] != max(s1) and snp[0] != min(s1)):
        gcnt += 1
        print(num)

print(f"gcnt: {gcnt}")

# gcnt: 2004