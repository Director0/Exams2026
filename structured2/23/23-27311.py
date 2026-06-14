def f(curr, end):
    if curr < end:
        return 0
    if curr == end:
        return 1

    return f(curr - 2, end) + f(curr - 3, end) + f(curr // 5, end)

print(f(63, 47) * f(47, 3) + f(63, 25) * f(25, 3) - 2*(f(63, 47) * f(47, 25) * f(25, 3)))

