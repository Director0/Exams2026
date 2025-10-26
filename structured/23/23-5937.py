


def c(curr, end, tl):
    if curr > end:
        return 0
    if curr == end and len([n for n in tl if n % 2 == 0]) <= 15:
        return 1

    return c(curr + 2, end, tl + [curr + 2]) + c(curr + 3, end, tl + [curr + 3]) + c((curr * 2) + 1, end, tl + [(curr * 2) + 1])


print(c(1, 55, [1]))
