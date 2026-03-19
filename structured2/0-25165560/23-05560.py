def f(curr, end, m):
    if curr > end:
        return 0
    if curr == end and (14 in m or 21 in m):
        return 1

    return f(curr + 2, end, m + [curr + 2]) + f(curr + 3, end, m + [curr + 3]) + f(curr * 2, end, m + [curr * 2])


print(f(7, 32, []))