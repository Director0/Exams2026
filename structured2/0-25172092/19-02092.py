from functools import lru_cache

def moves(s):
    if s >= 4 and s % 3 == 0:
        return (s - 1), (s - 4), (s // 3)
    elif s >= 4:
        return (s - 1), (s - 4)
    elif s % 3 == 0:
        return (s - 1), (s // 3)
    else:
        return [s - 1]


@lru_cache(maxsize=None)
def play(s):
    if s <= 1:
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


print(19, [s for s in range(101, 4, -1) if play(s) in "P1"])
print(19, [s for s in range(101, 4, -1) if play(s) in "V2"])
print(19, [s for s in range(101, 4, -1) if play(s) in "P2"])