def f(curr, end, pat):
    if curr > end or pat.count("*2") > 1:
        return 0
    if curr == end and pat.count("*2") == 1:
        return 1

    return f(curr + 1, end, pat + "+1") + f(curr + 2, end, pat + "+2") + f(curr * 2, end, pat + "*2")

print(f(2, 12, ""))