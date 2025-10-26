def c(curr, end):
    if curr > end or curr == 35:
        return 0
    if curr == end:
        return 1
    if curr < end:
        return c(curr + 1, end) + c(curr + 2, end) + c(curr * 2 , end)

print(c(7, 13) * c(13, 15) * c(15, 51))