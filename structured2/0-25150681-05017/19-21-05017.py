from functools import lru_cache


def moves(s):
    return s + 2, s + 4, s * 2


@lru_cache(maxsize=None)
def play(s):
    if s >= 100:
        return "V0"
    if all(play(t) in "V0" for t in moves(s)):
        return "P1"
    if any(play(t) in "P1" for t in moves(s)):
        return "V1"
    if all(play(t) in "V0V1" for t in moves(s)):
        return "P2"
    if any(play(t) in "P2" for t in moves(s)):
        return "V2"
    if all(play(t) in "V0V1V2" for t in moves(s)):
        return "P3"
    else:
        return "?"


print(19, [s for s in range(1, 99) if play(s) in "V1"])
print(20, [s for s in range(1, 99) if play(s) in "P3"])
print(21, [s for s in range(1, 99) if play(s) in "V2"])