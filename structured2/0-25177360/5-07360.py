def f(curr, end, m):
    if curr > end or len(m) > 4:
        return 0
    if curr == end:
        return 1

    return f(curr + 8, end, m + "1") + f(curr * 2, end, m + "2")


print(f(45, 376, ""))

