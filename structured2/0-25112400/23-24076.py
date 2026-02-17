def f(curr, end):
    if curr < end or curr == 22:
        return 0
    if curr == end:
        return 1

    return f(curr - 2, end) + f(curr - 5, end) + f(curr // 2, end)

print(f(47, 11))