from functools import lru_cache

def moves(s):
    mvs = []

    for n in range(100, 1, -1):
        if sum(mvs) < 80 and s * n < 80 and sum(mvs) + (s + (s * n)) <= 80:
            mvs.append(s + (s * n))

    mvs.append(s + 10)
    mvs.append(s + 2)

    return mvs

print(moves(1))
@lru_cache(maxsize=None)
def play(s):
    if s >= 166:
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


print(19, [s for s in range(1, 200) if any(play(t) in "V1" for t in moves(s))])
print(19, [s for s in range(1, 200) if play(s) in "V2"])
print(19, [s for s in range(1, 200) if play(s) in "P2"])