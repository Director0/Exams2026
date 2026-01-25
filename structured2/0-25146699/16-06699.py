def f(n):
    if n < 4:
        return n - 1

    if n > 3 and n % 3 == 0:
        return n + 2 * f(n - 1)

    if n > 3 and n % 3 != 0:
        return f(n - 2) + f(n - 3)

print(f(25))