

def c(curr, end, t):
    if t[-3:] == "AAA":
        return 0
    if curr > end + 5:
        return 0
    if curr == end:
        return 1
    return c(curr - 1, end, t + "A") + c(curr + 5, end, t + "B") + c(curr * 1, end, t + "C")

print(c(5, 34, ""))