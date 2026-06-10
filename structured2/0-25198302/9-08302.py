f = open("9_08302.txt")

data = [list(map(int, a.split())) for a in f]
print(data)
ls10 = [[x[0], x[1], x[2],(2 * x[0] * x[1] + 2 * x[1] * x[2] + 2 * x[0] * x[2]) / 10_000] for x in data if (2 * x[0] * x[1] + 2 * x[1] * x[2] + 2 * x[0] * x[2]) / 10_000 < 10]
lsx10 = [[x[0], x[1], x[2],(2 * x[0] * x[1] + 2 * x[1] * x[2] + 2 * x[0] * x[2]) / 10_000] for x in data if (2 * x[0] * x[1] + 2 * x[1] * x[2] + 2 * x[0] * x[2]) / 10_000 >= 10]


print(len(ls10))
print(len(lsx10))

print(len(ls10) / 191)
print(len(lsx10) / 103)