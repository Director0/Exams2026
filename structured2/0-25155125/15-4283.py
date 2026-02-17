p = [1, 3, 4, 9, 11, 13, 15, 17, 19, 21]
q = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
a = []

for x in range(1, 100):
    if not (((x in p) <= (x in a)) or ((x not in a) <= (x not in q))):
        a.append(x)


print(a)