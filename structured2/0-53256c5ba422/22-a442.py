def f(curr, end):
    if curr > end or curr == 23:
        return 0
    if curr == end:
        return 1

    return f(curr + 1, end) + f(curr + 3, end) + f(curr * 4, end)


print(f(4, 18) * f(18, 35))