def f(curr, end):
    if curr > end or curr == 22:
        return 0
    if curr == end:
        return 1

    return f(curr + 2, end) + f(curr + 3, end) + f(curr + (int(str(curr)[-1]) if int(str(curr)[-1]) > 5 else int(str(curr)[-2])), end)


print(f(13, 35) * f(35, 41))