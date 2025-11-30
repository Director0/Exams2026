def f(n):
    if n >= 5000:
        return 2

    if n < 5000:
        return f(n + 5) + 3

def g(n):
    if n < 20:
        return n

    if n >= 20:
        return g(n - 5) + 4


print(abs(f(25) - g(4000)))