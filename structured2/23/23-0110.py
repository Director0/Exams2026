res = []

def f(curr, cm):
    if len(cm) > 5:
        return 0
    if len(cm) == 5:
        res.append(curr)

    f(curr + 4, cm + "4")
    f(curr * 2, cm + "2")

f(2, "")


print(set(res))
print(len(set(res)))
