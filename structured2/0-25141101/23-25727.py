def f(curr, end):
    if curr < end or 30 <= curr <= 45:
        return 0
    if curr == end:
        return 1

    return f(curr - 4, end) + f(curr - 11, end) + f(curr // 2, end)


print(f(120, 20))