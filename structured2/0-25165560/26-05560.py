f = open("26.txt")

# 1111
s1 = [0] * 60
s2 = [0] * 25
s3 = [0] * 15

nopark = 0
parkstand = 0

data = []


for s in f:
    ls = list(map(int, s.split()))

    data.append(ls)

data.sort()
print(data)

for beg, ts, cls in data:
    fl = False

    if cls == 1:
        for i in range(len(s1)):
            if s1[i] <= beg:
                s1[i] = beg + ts
                fl = True
                break

        if fl == False:
            for i in range(len(s2)):
                if s2[i] <= beg:
                    s2[i] = beg + ts
                    fl = True
                    break

    elif cls == 2:
        for i in range(len(s2)):
            if s2[i] <= beg:
                s2[i] = beg + ts
                fl = True
                break

    else:
        for i in range(len(s3)):
            if s3[i] <= beg:
                s3[i] = beg + ts
                fl = True
                break

        if fl == False:
            for i in range(len(s1)):
                if s1[i] <= beg:
                    s1[i] = beg + ts
                    fl = True
                    parkstand += 1
                    break

    if fl == False:
        nopark += 1


print(nopark)
print(parkstand)

# функция (парковка, вр нач, вр ок) воозвр истину/ложь в зависимости от постановки
