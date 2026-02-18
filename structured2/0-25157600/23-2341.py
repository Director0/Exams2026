def f(curr, end, cc):
    if curr > end or cc > 8:
        return 0
    if curr == end and cc == 8:
        return 1

    return f(curr + 1, end, cc + 1) + f(curr + 5, end, cc + 1) + f(curr * 3, end, cc + 1)

cnt = 0

for i in range(1000, 1024 + 1):
    if f(1, i, 0) != 0:
        print(i)