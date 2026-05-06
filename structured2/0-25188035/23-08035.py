from functools import cache


@cache
def f(curr, end):
    if curr > end:
        return 0
    if curr == end:
        return 1

    return f(curr + 1, end) + f(curr + (curr + 1) if curr % 2 == 0 else curr + (curr + 2), end) + f(curr * 2, end)

print(f(3, 25) * f(25, 75))