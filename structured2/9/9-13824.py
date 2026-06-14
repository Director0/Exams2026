f = open("9_13824.txt")

num = 0
smx = 0

for s in f:
    num += 1
    ls = list(map(int, s.split()))
    lx = ""

    sp = [x for x in ls if ls.count(x) >= 2]
    snp = [x for x in ls if ls.count(x) == 1]
    spx = 1

    for i in range(len(ls)):
        if ls[i] % 2 == 0:
            lx += "*"
        else:
            lx += "$"

    if len(sp) != 0:
        for x in sp:
            spx *= x

    if (lx == "*$*$*$*" or lx == "$*$*$*$") and sum(snp) * 3 >= spx:
        print(num, ls)
        smx += num

print(smx)