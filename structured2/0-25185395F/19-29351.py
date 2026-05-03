from functools import lru_cache

def moves(s):
    a, b = s

    return (a + 4, b), (a, b + 4), (a * 3, b), (a, b * 3)


@lru_cache(maxsize=None)
def play(s):
    if sum(s) >= 154:
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


print(19, [s for s in range(1, 143) if any(play(t) in "V1" for t in moves((11, s)))])
print(20, [s for s in range(1, 143) if play((11, s)) in "V2"])
print(20, [s for s in range(1, 143) if play((11, s)) in "P2"])
