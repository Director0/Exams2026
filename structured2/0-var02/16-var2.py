from sys import setrecursionlimit

setrecursionlimit(50000)

def f(n):
    if n < 3:
        return 3
    else:
        return 2*n + 6 + f(n - 2)


print(f(3027) - f(3023))