from sys import setrecursionlimit

setrecursionlimit(100000)


def f(curr, end):
    if curr < end:
        return 0
    if curr == end:
        return 1

    return f(curr - 2, end) + f(int(str(curr)[::-1]) if int(str(curr)[-1]) < int(str(curr)[0]) else 0, end)


print(f(49, 12))