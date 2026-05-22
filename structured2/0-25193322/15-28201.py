from functools import lru_cache

@lru_cache(maxsize=None)
def f(x, y, z, a):
    return ((z % 115 == 0) and (y % 78 == 0) and (x % 51 == 0)) <= ((x*y*z) % a == 0)


for a in range(1_000_000, 1, -1):
    if all(f(x, y, z, a) for x in range(1, 100) for y in range(1, 100) for z in range(1, 100)):
        print(a)