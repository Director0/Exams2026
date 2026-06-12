def f(curr, end):
    if curr > end:
        return 0
    if curr == end:
        return 1

    return f(curr + 2, end) + f(curr + 3, end) + f(int(str(curr) + "1"), end)


print(f(3, 12) * f(12, 25))