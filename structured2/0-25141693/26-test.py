f = open("26_00.txt")

# 4997 2612 87 52

ls = [int(x) for x in f]
ls.sort()

k = 0
r = ls[0]

s = 26
c = 3
d = 6

lns = []

for n in ls:
    if n > (r + d + k):
        r = n
        k += 1

        if n == s:
            break
        elif n > s:
            k -= 1
            break


for k1 in range(k + 1):
    r = s
    k = k1

    for n in ls:
        if n > (r + d + k):
            r = n
            k += 1

    if k + 1 >= c:
        lns.append(k + 1)


print(max(lns))
print(len(lns))