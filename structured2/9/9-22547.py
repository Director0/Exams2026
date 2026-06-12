f = open("9_22547.txt")


cnt = 0
num = 0

for s in f:
    num += 1
    ls = list(map(int, s.split()))

    if ls == sorted(ls) and len([x for x in ls if x % 2 == 0]) == len([x for x in ls if x % 2 != 0]):
        cnt += 1
        print(num, sum(ls), ls)


print(cnt)