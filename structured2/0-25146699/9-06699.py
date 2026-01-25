f = open("9_06699.txt")

cnt = 0

for s in f:
    s1 = list(map(int, s.split()))

    st = [x for x in s1 if x % 2 == 0]
    snt = [x for x in s1 if x % 2 != 0]

    if sum(snt) > sum(st):
        cnt += 1

print(cnt)