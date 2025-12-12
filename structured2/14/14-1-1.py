from functools import lru_cache

@lru_cache(maxsize=None)
def convert(num, n):
    res = ""

    while n != 0:
        res += str(num % n)

        num //= n

    return res[::-1]


for i in range(200):
    i1 = convert(i, 4)

    if i1[-1:-4] == "123":
        print(i1)