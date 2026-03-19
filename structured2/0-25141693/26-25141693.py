f = open("26.txt")

stud = {}
tasks = {}

# 40421

for s in f:
    id, num = list(map(int, s.split()))

    if id in stud:
        stud[id].add(num)
    else:
        stud[id] = set()
        stud[id].add(num)

    if num in tasks:
        tasks[num].add(id)
    else:
        tasks[num] = set()
        tasks[num].add(id)


for x in stud:
    stud[x] = {a for a in stud[x] if len(tasks[a]) == 1}

maxl = 0

for x, y in sorted(stud.items()):
    if len(y) >= maxl:
        maxl = len(y)
        k = x


print(k)
print(maxl)

