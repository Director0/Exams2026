from sys import setrecursionlimit

setrecursionlimit(100000)


def f(curr, end):
    if curr == end:
        return 1
    elif curr > end + 2 or curr % 3 == 0:
        return 0

    return f(curr - 1, end) + f(curr + 3, end) + f(curr * 2, end)

print(f(5, 100))