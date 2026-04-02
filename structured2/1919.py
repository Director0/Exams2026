from functools import lru_cache


def moves(s):
    a, b = s
    mvs = []

    if a > 3:
        mvs.append((a - 3, b))
    if b > 3:
        mvs.append((a, b - 3))

    if a > 0:
        mvs.append((a // 2, b))
    if b > 0:
        mvs.append((a, b // 2))

    return mvs


@lru_cache(maxsize=None)
def play(s):
    if sum(s) <= 100:
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


print(19, [s for s in range(52, 300) if any(play(t) in "V1" for t in moves((48, s)))])
print(20, [s for s in range(52, 300) if play((48, s)) in "V2"])
print(20, [s for s in range(52, 300) if play((48, s)) in "P2"])