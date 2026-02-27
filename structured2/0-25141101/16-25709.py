from sys import setrecursionlimit
setrecursionlimit(10000000)

def f(n):
    if n >= 14000:
        return f(n - 7) + 3 * n
    else:
        return g(n - 3) + 3 * n - 12


def g(n):
    if n < 80000:
        return 5 * n + g(n + 4)
    else:
        return 2 * n + 1


print(f(50000))