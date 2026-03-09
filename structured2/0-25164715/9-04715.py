f = open("9_04715.txt")

cnt = 0

for s in f:
    ls = list(map(int, s.split()))

    sp = set([x for x in ls if ls.count(x) == 2])

    if len(sp) == 2 and ls[0] == ls[2] and ls[1] == ls[3]:
        cnt +=1
        print(ls)


print(cnt)