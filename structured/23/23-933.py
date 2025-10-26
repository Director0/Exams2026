
res = set()

def c(curr):
    if (0 <= curr < 100) and curr % 2 == 0:
        res.add(curr)
    if curr > 100:
        return 0
    else:
        c(curr + 3)
        c(curr * 3)

c(3)

print(len(res))
print(res)