from functools import lru_cache


def moves(s):
    return s - 3, s - 5, s // 4


@lru_cache(maxsize=None)
def play(s):
    if s <= 30:
        return 0