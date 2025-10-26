
res = set()

def c(curr, tn):
    if tn == 13:
        if curr < 0:
            res.add(curr)
    else:
        c(curr - 3, tn + 1)
        c(curr * (-3), tn + 1)


c(333, 0)

print(len(res))
print(res)