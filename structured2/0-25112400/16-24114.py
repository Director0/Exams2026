from sys import setrecursionlimit

setrecursionlimit(100000000)


def g(n):
    if n >= 30000:
        return 3
    else:
        return g(n + 3) + 7




print(g(1501))