def f(curr, end, cprev):
    if curr > end or (4030 in cprev and 60 in cprev):
        return 0
    if curr == end and (4030 in cprev or 60 in cprev):
        return 1

    return f(curr + 1, end, cprev + [curr + 1]) + f(curr * 2, end, cprev + [curr * 2]) + f(curr * 3, end, cprev + [curr * 3])

print(f(10, 70, []))