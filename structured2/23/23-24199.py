
def f(curr, end, tl):
    if (curr < end) or (len([x for x in tl if x % 6 == 0]) > 0):
        return 0
    if  curr == end:
        return 1

    return f(curr - 1, end, tl + [curr - 1]) + f(curr // 3, end, tl + [curr // 3]) + f(curr // 4, end, tl + [curr // 4])


print(f(100, 33, [100]) * f(33, 1, [33]))