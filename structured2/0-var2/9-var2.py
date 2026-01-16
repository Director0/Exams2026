f = open("9-0.txt")

num = 0
gcnt = 0


for s in f:

    num += 1
    s1 = list(map(int, s.split()))

    s2 = sorted(s1)[1:7]

    if (s1 == sorted(s1, reverse=True)) and (((max(s1) + min(s1)) / 2) > (sum(s2) / len(s2))):
        gcnt += 1
        print(num)
        print(sum(s1))
        break

print(f"gcnt: {gcnt}")

# gcnt: 2004