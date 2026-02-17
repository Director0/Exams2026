s = open("26_18492.txt")

tm = [0] * 1440

for a in s:
    l = list(map(int, a.split()))

    for x in range(l[1], l[2]):
        tm[x] += 1


print(tm)
print(max(tm))

for i in range(len(tm)):
    if tm[i] == 548:
        print(i)

sum1 = 0
