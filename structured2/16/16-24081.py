import sys

sys.setrecursionlimit(5000)

def f(n):
    return g(n - 50000) + g(n + 50000)

def g(n):
    if n > 6:
        return g(n - 3) + 2
    else:
        return 5 ** n




print(f(100000))