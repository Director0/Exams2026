from functools import lru_cache


def moves(s):
    a, b = s
    return (a + 1, b), (a, b + 1), (a * 2, b), (a, b * 2)


@lru_cache(maxsize=None)
def play(s):
    if sum(s) >= 107:
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


print(19, [s for s in range(1, 94) if any(play(t) in "V1" for t in moves((13, s)))])
print(19, [s for s in range(1, 94) if play((13, s)) in "V2"])
print(19, [s for s in range(1, 94) if play((13, s)) in "P2"])