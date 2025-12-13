f = open("9-116acc.txt")

cnt = 0

for s in f:
    s1 = list(map(int, s.split()))
    s1.remove(max(s1))
    s1.remove(min(s1))

    if (sum(s1) / len(s1)) >= 8:
        cnt += 1

print(cnt)