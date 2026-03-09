def f(curr, end, m):
    if curr > end or "BB" in m:
        return 0
    if curr == end:
        return 1

    return f(curr + 2, end, m + "A") + f(curr ** 2, end, m + "B") + f(curr * 3, end, m + "C")


print(f(2, 64, ""))