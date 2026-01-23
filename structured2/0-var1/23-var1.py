def f(curr, end):
    if curr > end or curr == 26:
        return 0
    if curr == end:
        return 1

    return f(curr + 1, end) + f((2 * curr) + 1, end)


print(f(1, 27))