from functools import lru_cache


#Сумма углов невырожденного треугольнгика: 180

@lru_cache(maxsize=None)
def angle(a, b, c):
    if (a + b + c) == 180:
        return True
    else:
        return False


def f(x):
    return ((angle(37, a, x + 45)) == (angle(a, x, 90)) and (not(a + 23 < 120)) )


for a in range(1, 100):
    if all(f(x) for x in range(1, 1000)):
        print(a)