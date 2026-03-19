f = open("26--10.txt")


# 1000 400 100

persons = 8
limit = 4
univs = 4

data = []
nstudents = [0] * univs

un_stud = {}
d1 = dict.fromkeys([str(x) for x in range(101)], [])
un_stud.update(d1)

employees = []

for s in f:
    ls = list(map(int, s.split()))
    data.append(ls)



# ///////


for pers in data:
    pid, uid, score, contr = pers

    if contr == 1 and len(employees) < limit:
        nstudents[uid] += 1
        employees.append(pers)

for pers in employees:
    data.remove(pers)


for pers in data:
    pid, uid, score, contr = pers

    if contr == 1 and len(employees) < limit:
        nstudents[uid] += 1
        employees.append(pers)


print(len(employees))
print(un_stud)
print(max(data, key=lambda x:x[2]))


for pers in data:
    pid, uid, score, contr = pers

    un_stud.setdefault(str(uid), []).append(score)
    data.remove(pers)

for pers in data[:]:   # copy of list
    ...
    data.remove(pers)

# print(nstudents)
# print(un_stud)
print(un_stud)