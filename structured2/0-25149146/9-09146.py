f = open("9_09146.txt")

res = []

for s in f:
    ls = list(map(int, s.split()))

    sn = 1

    for x in ls:
        sn *= x

    if (str(max(ls))[-1] == str(min(ls))[-1]) and (sum(ls) > sn):
        res += ls

print(res)
print(sum(res) / len(res))
print(int(abs(sum(res) / len(res))))