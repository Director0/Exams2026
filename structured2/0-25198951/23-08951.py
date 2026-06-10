def f(curr, end, m):
    if curr > end or m.count("C") > 2:
        return 0
    if curr == end and m.count("C") <= 2:
        return 1

    return f(curr + 1, end, m + "A") + f(curr + 2, end, m + "B") + f(curr * 2, end, m + "C")


print(f(2, 12, ""))