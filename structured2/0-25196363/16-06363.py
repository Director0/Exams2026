from functools import lru_cache

@lru_cache(maxsize=None)
def f(n):
    if n < 2025:
        return n**2
    elif 2025 <= n < 2050:
        return 2 * f(n - 1) - f(n - 2) + n
    elif 2050 <= n <= 2100:
        return f(n - 1) + 2 * f(n - 2) + 3 * f(n - 3)
    elif n > 2100:
        return 2 * f(n - 1) + f(n - 2) + n


print(f(2020) + f(2200))