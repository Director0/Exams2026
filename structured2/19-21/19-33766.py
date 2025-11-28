from functools import lru_cache

def moves(s):
    a, b = s

    return (a + 1, b), (a, b + 1), (a + b, b), (a, b + a)

@lru_cache(maxsize=None)
def play(s):
    if sum(s) >= 67:
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

print(19, [s for s in range(1, 58) if play((9, s)) in "P1"])
print(20, [s for s in range(1, 58) if play((9, s)) in "V2"])
print(21, [s for s in range(1, 58) if play((9, s)) in "P2"])