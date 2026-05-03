f = open("26_28945 (1).txt")

data = [(start, end, dur) for (start, end, dur) in list(map(int, a.split()) for a in f)]

cnt = 992

for i in range(1, len(data)):
    if data[i][0] == data[i - 1][1]:
        cnt -= 2
    elif data[i][0] < data[i - 1][1]:
        cnt -= 1


print(cnt)