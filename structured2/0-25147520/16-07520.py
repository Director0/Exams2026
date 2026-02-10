from sys import setrecursionlimit

setrecursionlimit(100000)

def g(n):
    if n < 10:
        return n
    if n > 9:
       return n - 2 + f(n - 1)

def f(n):
    if n < 10:
        return n
    if n > 9:
       return 3 * n + g(n - 2)


print(f(2204) - g(2200))