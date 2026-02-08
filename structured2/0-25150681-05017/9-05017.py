f = open("9-05017.txt")

cnt = 0

for s in f:
    s1 = list(map(int, s.split()))

    if len([x for x in s1 if x % 3 == 0]) == 3 and (max(s1) - min(s1)) <= sum([x for x in s1 if x % 3 == 0]):
        cnt += 1

print(cnt)