from functools import lru_cache


def moves(s):
    a, b = s

    if a > 3 and b > 3:
        return (a - 3, b - 3), (a // 2, b), (a, b // 2)
    elif a == 0:
        return (a, b // 2)
    elif b == 0:
        return (a // 2, b)
    else:
        return ()



@lru_cache(maxsize=None)
def play(s):
    if 0 < sum(s) <= 200:
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


print(19, [s for s in range(125, 1000) if any(play(t) in "V1" for t in moves((76, s)))])
print(19, [s for s in range(125, 1000) if play((76, s)) in "V2"])
print(19, [s for s in range(125, 1000) if play((76, s)) in "P2"])