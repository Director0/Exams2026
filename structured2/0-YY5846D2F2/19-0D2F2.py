from functools import lru_cache

def moves(s):
    return s + 3, s * 2, s * 3


@lru_cache(maxsize=None)
def play(s):
    if 55 <= s <= 77:
        return "P0"
    elif s > 77:
        return "L0"
    elif any(play(t) in "P0" for t in moves(s)):
        return "V1"
    elif all(play(t) in "V1L0" for t in moves(s)):
        return "P1"
    elif any(play(t) in "P1" for t in moves(s)):
        return "V2"
    elif all(play(t) in "V1V2L0" for t in moves(s)):
        return "P2"
    else:
        return "?"


print(19, [s for s in range(1, 55) if play(s) in "P1"])
print(19, [s for s in range(1, 55) if play(s) in "V2"])
print(19, [s for s in range(1, 55) if play(s) in "P2"])