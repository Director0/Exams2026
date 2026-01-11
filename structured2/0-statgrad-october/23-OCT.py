def f(curr, end, c):
    if curr > end:
        return 0
    if curr == end and (24 in c or 27 in c):
        return 1

    return f(curr + 1, end, c + [curr + 1]) + f(curr * 2, end, c + [curr * 2]) + f(curr * 3, end, c + [curr * 3])


print(f(9, 81, []))


# def f(curr, end):
#     if curr > end:
#         return 0
#     if curr == end:
#         return 1
#
#     return f(curr + 1, end) + f(curr * 2, end) + f(curr * 3, end)
#
#
# a1 = f(9, 24) * f(24, 81)
# a2 = f(9, 27) * f(27, 81)
# a3 = f(9, 24) * f(24, 27) * f(27, 81)
#
# print((a1 + a2) - a3)

