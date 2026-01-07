def f(curr, end):
    if curr > end or curr == 50:
        return 0
    if curr == end:
        return 1

    return f(curr + 3, end) + f((2 * curr) + 1, end) + f((min([x for x in range(curr + 1, curr + 10) if x % 3 == 0])), end)

print(f(5, 23) * f(23, 89))