from functools import lru_cache

def moves(s):
    return s + 1, s * 3


@lru_cache(maxsize=None)
def play(s): # ваня
    if s >= 36:
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


@lru_cache(maxsize=None)
def play1(s): # петя
    if s <= 85:
        return "V0"
    elif all(play(t) in "V0" for t in moves(s)):
        return "P1"
    elif any(play(t) in "P1" for t in moves(s)):
        return "V1"
    elif all(play(t) in "V1" for t in moves(s)):
        return "P2"
    elif any(play(t) in "P1P2" for t in moves(s)):
        return "V2"
    elif all(play(t) in "V0V1V2" for t in moves(s)):
        return "P3"
    else:
        return "?"

print(play(10))
print(play1(10))
