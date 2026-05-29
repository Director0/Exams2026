from functools import lru_cache

def moves(s):
    return s - 7, s // 3


@lru_cache(maxsize=None)
def play(s):
    if 0 <= s <= 116:
        return "P0"
    elif any(play(t) in "P0" for t in moves(s)):
        return "V1"
    elif all(play(t) in "V1" for t in moves(s)):
        return "P1"
    elif any(play(t) in "P1" for t in moves(s)):
        return "V2"
    elif all(play(t) in "V1V2" for t in moves(s)):
        return "P2"
    elif any(play(t) in "P2" for t in moves(s)):
        return "V3"
    elif all(play(t) in "V1V2V3" for t in moves(s)):
        return "P3"
    else:
        return "?"


print(19, [s for s in range(117, 10_001) if any(play(t) in "P0" for t in moves(s))])
print(19, [s for s in range(117, 10_001) if play(s) in "V2"])
print(19, [s for s in range(117, 10_001) if play(s) in "P2"])