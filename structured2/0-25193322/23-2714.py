def f(curr, end, m):
    if curr > end or len([x for x in m if x % 2 == 0]) > 6:
        return 0
    if curr == end and len([x for x in m if x % 2 == 0]) == 6:
        return 1

    return f(curr + 1, end, m + [curr]) + f(curr + 3, end, m + [curr]) + f(curr + 5, end, m + [curr])

print(f(3, 25, []))