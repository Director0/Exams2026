from functools import lru_cache

def moves(s):
    return s + 1, s + 2, s + 3


@lru_cache(maxsize=None)
def play(s):
    if s >= 21:
        return "P0"
    if any(play(t) in "P0" for t in moves(s)):
        return "V1"
    if all(play(t) in "V1" for t in moves(s)):
        return "P1"
    if any(play(t) in "P1" for t in moves(s)):
        return "V2"
    if all(play(t) in "V1V2" for t in moves(s)):
        return "P2"
    if any(play(t) in "P2" for t in moves(s)):
        return "V3"
    if all(play(t) in "V1V2V3" for t in moves(s)):
        return "P3"
    else:
        return "?"


print(19, [s for s in range(1, 20) if play(s) in "P1"])
print(19, [s for s in range(1, 20) if play(s) in "V3"])
print(19, [s for s in range(1, 20) if play(s) in "P3"])