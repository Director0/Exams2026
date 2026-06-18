f = open("26_7014.txt")

data = [int(x) for x in f]

num = 0
rx = 1

for i in range(len(data)):
    num += 1

    if data[i] == 500:
      rx += (num * data[i])
      num = 0


print(rx)
