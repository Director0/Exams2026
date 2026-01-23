def f(curr, end):
    if curr > end or curr == 10:
        return 0
    if curr == end:
        return 1

    return f(curr + 1, end) + f(curr + 2, end) + f(curr * 2, end)

print(f(3, 7) * f(7, 20))