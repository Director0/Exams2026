def f(x, y):
    if x > y:
        return 0

    if x == y:
        return 1

    if int(str(x)[-2]) < int(str(x)[-1]):
        return f(x + 1, y) + f(int(str(x)[0] + str(x)[-1] + str(x)[-2]), y)

    return f(x + 1, y)


print(f(101, 154))
