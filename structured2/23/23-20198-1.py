def f(curr, end, cm):
    if "AAA" in cm or curr > end + 2:
        return 0

    if curr == end and "AAA" not in cm:
        return 1

    return f(curr - 1, end, cm + "A") + f(curr + 5, end, cm + "B") + f(curr * 2, end, cm + "C")


print(f(5, 34, ""))