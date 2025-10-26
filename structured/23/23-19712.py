def c(curr, end, t):
    if "AAA" in t or "BBB" in t:
        return 0
    if curr < end:
        return 0
    if curr == end:
        return 1
    if curr > end:
        return c(curr - 2, end, t + "A") + c(curr // 2 if curr % 2 == 0 else curr - 7, end, t + "B")

print(c(40, 1, ""))