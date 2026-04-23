def f(curr, end):
    if curr < end or curr == 73:
        return 0
    if curr == end:
        return 1

    return f(curr - 3, end) + f(curr - 8, end) + f(curr // 2, end)


print(f(76, 41) * f(41, 12))