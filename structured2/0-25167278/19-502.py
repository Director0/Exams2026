from functools import lru_cache

def moves(s):
    a, b = s

    return (a + 3, b), (a, b + 3), (a * 2, b), (a, b * 2)


@lru_cache(maxsize=None)
def play(s):
    if any(x >= 21 for x in s):
        return "P0"
    elif any(play(t) in "P0" for t in moves(s)):
        return "V1"
    elif all(play(t) in "V1" for t in moves(s)):
        return "P1"
    elif any(play(t) in "P1" for t in moves(s)):
        return "V2"
    elif all(play(t) in "V1V2" for t in moves(s)):
        return "P2"
    elif any(play(t) in "P1P2" for t in moves(s)):
        return "V3"
    elif all(play(t) in "V1V2V3" for t in moves(s)):
        return "P3"
    elif any(play(t) in "P1P2P3" for t in moves(s)):
        return "V4"
    elif all(play(t) in "V1V2V3V4" for t in moves(s)):
        return "P4"
    else:
        return "?"


print(19, [s for s in range(1, 100) if play((5, s)) in "V2"])
print(19, [s for s in range(1, 100) if play((4, s)) in "P2P3"])
print(19, [s for s in range(1, 100) if play((3, s)) in "V2V3V4"])