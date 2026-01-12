f = open("9-5.txt")

num = 0
gcnt = 0


for s in f:

    num += 1
    s1 = list(map(int, s.split()))

    sp = set([b for b in s1 if s1.count(b) == 4])
    snp = [b for b in s1 if s1.count(b) == 1]

    if (len(sp) == 1 and len(snp) == 3) and (sum(snp) / len(snp)) < (sum(s1) / len(s1)):
        gcnt += 1
        print(num)

print(f"gcnt: {gcnt}")

# gcnt: 2004