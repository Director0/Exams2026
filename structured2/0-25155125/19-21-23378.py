from functools import lru_cache

def moves(s):
    return s - 3, s - 6, s // 3


@lru_cache(maxsize=None)
def play(s):
    if s <= 27:
        return "P0"
    if any(play(t) in "P0" for t in moves(s)):
        return "V1"
    if all(play(t) in "V1" for t in moves(s)):
        return "P1"
    if any(play(t) in "P1" for t in moves(s)):
        return "V2"
    if all(play(t) in "V1V2" for t in moves(s)):
        return "P2"
    else:
        return "?"


print(19, [s for s in range(28, 200) if play(s) in "P1"])
print(20, [s for s in range(28, 200) if play(s) in "V2"])
print(21, [s for s in range(28, 200) if play(s) in "P2"])