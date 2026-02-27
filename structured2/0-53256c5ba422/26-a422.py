f = open("26.txt")


# 1000 400 100

persons = 1000
limit = 400
univs = 101

data = []
nstudents = [0] * univs
un_stud = []
employees = []

for s in f:
    ls = list(map(int, s.split()))
    data.append(ls)


for pers in data:
    pid, uid, score, contr = pers

    if contr == 1 and len(employees) < limit:
        nstudents[uid] += 1
        employees.append(pers)
        data.remove(pers)

for pers in data:
    pid, uid, score, contr = pers

    if contr == 1 and len(employees) < limit:
        nstudents[uid] += 1
        employees.append(pers)
        data.remove(pers)

for pers in data:
    pid, uid, score, contr = pers

    if contr == 1 and len(employees) < limit:
        nstudents[uid] += 1
        employees.append(pers)
        data.remove(pers)

for pers in data:
    pid, uid, score, contr = pers

    if contr == 1 and len(employees) < limit:
        nstudents[uid] += 1
        employees.append(pers)
        data.remove(pers)
print(len(employees))


for pers in data:
    pid, uid, score, contr = pers

    if nstudents[uid] < 1 and len(employees) < limit:
        nstudents[uid] += 1
        cand = max([x for x in data if x[1] == uid], key=lambda x:x[2])
        employees.append(cand)
        data.remove(cand)

print(data)
print(len(employees))
print(nstudents.count(1))

print(max(data, key=lambda x:x[2]))