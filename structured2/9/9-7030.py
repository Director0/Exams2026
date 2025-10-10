f = open("9_7030.txt")

cnt = 0


for s in f:

    s1 = list(map(int, s.split()))
    nums3 = []

    for n in s1:
        if s1.count(n) == 2 and n not in nums3:
            nums3.append(n)

    if len(nums3) == 3:
        for n in s1:
            l1 = s1.remove(n)

            if n ** 2 == s1[0] ** 2 + s1[1] ** 2:
                cnt += 1


print(cnt)