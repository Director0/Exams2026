

res = set()

def c(curr, tn):
    if tn == 8:
        if curr in range(1000, 1024):
            res.add(curr)

    else:
        c(curr + 1, tn + 1)
        c(curr + 5, tn + 1)
        c(curr * 3, tn + 1)

c(1, 0)

print(len(res))
print(res)