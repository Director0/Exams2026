def c(curr, end, tl):
    if (curr > end) or (curr == end and 20 in tl and 30 in tl):
        return 0
    if curr == end and (20 in tl or 30 in tl):
        return 1

    return c(curr + 3, end, tl + [curr + 3]) + c(curr + 5, end, tl + [curr + 5]) + c(curr * 2, end, tl + [curr * 2])


print(c(10, 40 , [10]))