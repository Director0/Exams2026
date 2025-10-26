from functools import lru_cache


res = set()

@lru_cache(maxsize=None)
def c(curr, tn):
    if tn == 68:
        res.add(curr)
    else:
        c(curr + 3, tn + 1)
        c(curr - 2, tn + 1)

c(1, 0)
print(len(res))
print(res)
