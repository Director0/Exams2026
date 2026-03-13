f = open("26_2651.txt")

yrs = {}
# yrs = yrs.fromkeys([str(x) for x in range(1961, 1992)], set()) NO NO NO NO NO DOOOONT USE THIS
cnt = 0
s1 = {1, 2, 3, 4, 5, 6, 7, 8}



for s in f:
    ls = list(map(int, s.split()))

    if str(ls[0]) in yrs:
        yrs[str(ls[0])].add(ls[1])
    else:
        yrs[str(ls[0])] = set()
        yrs[str(ls[0])].add(ls[1])

print(sorted(yrs.items()))

minl = 10000

for x, y in yrs.items():
    if len(y) <= minl:
        minl = len(y)
        k = x

    cnt += (len(s1) - len(y))

print(cnt)
print(k)