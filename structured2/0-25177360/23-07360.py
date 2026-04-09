def f(curr, end, m):
    if curr > end or curr < -12 or m.count("A") > 2:
        return 0
    if curr == end:
        return 1

    return f(curr - 2, end, m + "A") + f(curr * 2, end, m + "B") + f(curr * 3, end, m + "C")


print(f(6, 48, ""))