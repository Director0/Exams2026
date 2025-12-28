f = open("9-4.txt")

num = 0
gcnt = 0


for s in f:

    num += 1
    s1 = list(map(int, s.split()))

    sp = set([b for b in s1 if s1.count(b) == 3])
    snp = [b for b in s1 if s1.count(b) == 1]

    if (len(sp) == 1 and len(snp) == 3) and (3 * (sum(sp)**2) > (snp[0] ** 2 + snp[1] ** 2 + snp[2] ** 2)):
        print(num)
        gcnt +=1

print(f"gcnt: {gcnt}")

# gcnt: 245