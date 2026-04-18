f = open("9_00377.txt")

cnt = 0

for s in f:
    s1 = sorted(list(map(int, s.split())))

    if len(s1) == len(set(s1)) and (s1[0] + s1[-1])*3 >= (s1[1] + s1[2] + s1[3])*2:
        cnt += 1


print(cnt)