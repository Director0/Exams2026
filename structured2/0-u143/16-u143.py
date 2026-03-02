from sys import setrecursionlimit

setrecursionlimit(1000000)


def f(n):
    if n == 1:
        return 1

    if n > 1:
        return n * f(n - 1)


print((2026 * f(2029) + f(2028)) / f(2027)  )