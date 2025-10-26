def c(curr, end):
    if curr < end or curr == 13:
        return 0
    if curr == end:
        return 1
    if curr > end:
        return c(curr - 1, end) + c(curr - 2, end) + c(curr // 3, end)

print(c(19, 6) * c(6, 4))