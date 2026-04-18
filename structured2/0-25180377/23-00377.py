def conv(num, n):
    res = ""

    while num != 0:
        res += str(num % n)
        num //= n

    return res[::-1]

def f(curr, end):
    if int(curr, 2) > int(end, 2):
        return 0
    if int(curr, 2) == int(end, 2):
        return 1

    return f(conv(int(curr, 2) + 1, 2), end) + f(curr + "0", end) + f(curr + "1", end)


print(f("100", "11101"))