def f(curr, end):
    if curr < end:
        return 0
    if curr == end:
        return 1

    if curr % 3 == 0:
        return f(curr - 5, end) + f(curr // 3, end)
    else:
        return f(curr - 5, end) + f(curr - (curr % 3), end)

print(f(103, 73) * f(73, 24))