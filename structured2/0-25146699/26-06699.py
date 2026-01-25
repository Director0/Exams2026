f = open("26.txt")

ls = [int(s) for s in f]

ls.sort()

c = 0
nc = 0

for x in ls:
    if x % 2 == 0:
        c +=1
    else:
        nc -= 1

print(c, nc)