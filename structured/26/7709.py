f = open("26_7709.txt")

k = int(f.readline())
n = int(f.readline())

t = [[int(x) for x in s.split()] for s in f]

def isInnr(t1, t2):
    s1, e1 = t1
    s2, e2 = t2

    if max(s1, s2) > min(e1, e2):
        return False
    else:
        return True


cells = [[] for _ in range(k)]
count = 0
last = []

for beg, end in t:
    for i in range(k):
        if all(isInnr([beg, end], g) == False for g in cells[i]):
            count += 1
            cells[i].append([beg, end])
            last.append(i + 1)
            break


print(count, last[-2])