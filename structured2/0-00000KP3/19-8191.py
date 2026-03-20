from functools import lru_cache

def moves(s):
    return s + 1, s + 4, s * 2


@lru_cache(maxsize=None)
def play(s):
    if s >= 67:
        return "P0"
    elif any(play(t) in "P0" for t in moves(s)):
        return "V1"
    elif all(play(t) in "V1" for t in moves(s)):
        return "P1"
    elif any(play(t) in "P1" for t in moves(s)):
        return "V2"
    elif all(play(t) in "V1V2" for t in moves(s)):
        return "P2"
    else:
        return "?"


print(19, [s for s in range(1, 67) if play(s) in "P1"])
print(19, [s for s in range(1, 67) if play(s) in "V2"])
print(19, [s for s in range(1, 67) if play(s) in "P2"])