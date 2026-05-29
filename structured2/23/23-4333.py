def f(curr, end, m):
    if curr > end or curr == 6 or curr == 5:
        return 0
    if curr == end:
        return 1


    if m == []:
        return f(curr + 1, end, m + [1]) + f(curr + 3, end, m + [2]) + f(curr ** 2, end, m + [3])
    elif m[-1] == 1:
        return f(curr + 3, end, m + [2]) + f(curr ** 2, end, m + [3])
    elif m[-1] == 2:
        return f(curr + 1, end, m + [1]) + f(curr ** 2, end, m + [3])
    elif m[-1] == 3:
        return f(curr + 1, end, m + [1]) + f(curr + 3, end, m + [2])



print(f(1, 25, []))
# print(f(1, 5, []) * f(5, 25, []))