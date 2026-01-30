def f(curr, end):
    if curr > end or curr == 10:
        return 0
    if curr == end:
        return 1

    return f(curr + 3, end) + f((curr * 2) - 1, end)

print(f(2, 21) * f(21, 30))