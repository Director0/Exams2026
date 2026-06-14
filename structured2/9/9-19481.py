f = open("9_19481.txt")


num = 0
smx = 0

for s in f:
    num += 1
    ls = sorted(list(map(int, s.split())))

    sp = set([x for x in ls if ls.count(x) >= 2])

    if len(sp) == 0 and (ls[0] + ls[-1])**2 > ls[1]**3 + ls[2]**3:
        print(num, ls)
        smx += num

print(smx)