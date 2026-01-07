res = []

for n in range(100, 1001):
    res.append(int(f"{n:b}".replace("0", "")))

print(len(set(res)))
