from functools import lru_cache



def moves(s):
    a, b = s

    if a < b:
        return [(a + x, b) for x in range(1, a + 1)]
    elif b < a:
        return [(a, b + x) for x in range(1, b + 1)]
    else:
        return [(a + x, b) for x in range(1, a + 1)] + [(a, b + x) for x in range(1, b + 1)]


@lru_cache(maxsize=None)
def play(s):
    if sum(s) > 39:
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



print(19, min([sum((s, s1)) for s in range(1, 40) for s1 in range(1, 40) if play((s, s1)) in "V1"]))
print(19, [s for s in range(1, 40) if play((4, s)) in "V2"])
print(19, [s for s in range(1, 40) if play((4, s)) in "P2"])
