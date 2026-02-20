def f(curr, end):
    if curr < end or curr == 12:
        return 0
    if curr == end:
        return 1

    return f(curr - 3, end) + f(curr // 2, end)


print(f(80, 23) * f(23, 3))