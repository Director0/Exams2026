from functools import lru_cache
from math import ceil


def moves(s):
    a, b = s

    return (a - 2, b), (a, b - 2), ((ceil(a / 2) if a == max(a, b) else a), (ceil(b / 2) if b == max(a, b) else b))


@lru_cache(maxsize=None)
def play(s):
    if sum(s) <= 33:
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

print(play((23, 46)))

print(19, [s for s in range(11, 120) if any(play(t) in "V1" for t in moves((23, s)))])
print(19, [s for s in range(11, 120) if play((23, s)) in "V2"])
print(19, [s for s in range(11, 120) if play((23, s)) in "P2"])
