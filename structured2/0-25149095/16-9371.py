from sys import setrecursionlimit

setrecursionlimit(100000)

def f(n):
    if n >= 3210:
        return 1
    else:
        return f(n + 3) + 7

def g(n):
    if n >= 10:
        return g(n - 3) + 5
    else:
        return n


print(f(15) - g(3000))