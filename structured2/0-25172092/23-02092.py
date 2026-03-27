def f(curr, end, c):
    if curr > end:
        return 0
    if curr == end and all(x in c for x in "123"):
        return 1

    return f(curr + 1, end, c + "1") + f(curr + 2, end, c + "2") + f(curr * 2, end, c + "3")


print(f(3, 25, ""))