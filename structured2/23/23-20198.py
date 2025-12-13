def f(curr, end, cmds):
    if curr > end + 3:
        return 0
    elif curr == end:
        return 1
    else:
        if len(cmds) >= 2 and cmds[-2:] == "AA":
            return f(curr + 5, end, cmds + "B") + f(curr * 2, end, cmds + "C")
        else:
            return f(curr - 1, end, cmds + "A") + f(curr + 5, end, cmds + "B") + f(curr * 2, end, cmds + "C")

print(f(5, 34, ""))