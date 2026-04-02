def f(curr, end):
    if curr < end:
        return 0

    if curr == end:
        return 1

    return f(curr - 2, end) + (f(int(str(curr)[:-2] + str(curr)[-2::-1]), end) if len(str(curr)) > 1 and int(str(curr)[-1]) < int(str(curr)[-2]) else 0)

print(f(57, 13))