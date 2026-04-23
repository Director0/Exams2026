def f(curr, end, m):
    if curr > end:
        return 0
    if curr == end and len(set(m)) - 1 > 50:
        return 1

    return f(curr + 2, end, m + [curr]) + f(curr * 3, end, m + [curr]) + f(curr * 4, end, m + [curr])


print(f(2, 400, []))