from functools import lru_cache

def moves(s):
    a, b = s

    return (a - 1, b), (a, b - 1), (a // 2 if a % 2 == 0 and a != 1 else (a // 2) + 1, b), (a, b // 2 if b % 2 == 0 and a != 1 else (b // 2) + 1),

@lru_cache(maxsize=None)
def play(s):
    if sum(s) <= 20:
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

for s in range(1, 30 + 1):
    print(s, play((10, s)))


print(19, [s for s in range(1, 21) if any(play(x) in "P1" for x in moves((10, s)))])
