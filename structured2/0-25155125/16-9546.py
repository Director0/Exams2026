def f(n):
    if n >= 2222:
        return n
    else:
        return f(n + 5) + 7

print(f(45) - f(49))