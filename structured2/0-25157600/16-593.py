from functools import lru_cache

@lru_cache(maxsize=None)
def f(n):
    if n == 1:
        return 1

    if n > 1:
        return f(n - 1) - 2 * g(n - 1)

@lru_cache(maxsize=None)
def g(n):
    if n == 1:
        return 1

    if n > 1:
        return f(n - 1) + g(n - 1) + n


print(g(36))
print(sum([int(x) for x in str(g(36))]))