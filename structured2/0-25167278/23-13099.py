def f(curr, end, m):
    if curr > end + 16 or "AA" in m:
        return 0
    if curr == end:
        return 1

    return f(curr - 1, end, m + "A") + f(curr * 2, end, m + "B") + f(curr * 3, end, m + "C")


print(f(3, 15, ""))