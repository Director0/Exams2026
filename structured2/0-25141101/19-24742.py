from functools import lru_cache

def moves(s):
    a, b = s
    return (a + 20, b), (a, b + 20), (a * 3, b), (a, b * 3)


@lru_cache(maxsize=None)
def play(s):
    if sum(s) >= 841:
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


print(19, [s for s in range(1, 805) if any(play(t) in "V1" for t in moves((36, s)))])
print(19, [s for s in range(1, 805) if play((36, s)) in "V2"])
print(19, [s for s in range(1, 805) if play((36, s)) in "P2"])
