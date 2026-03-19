f = open("9_2043.txt")

cnt = 0

for s in f:
    ls = list(map(int, s.split()))

    if ls[0] == ls[2] and ls[1] == ls[3]:
       cnt += 1


print(cnt)