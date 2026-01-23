from functools import lru_cache
import sys
sys.setrecursionlimit(100000)

def moves(s):
    a, b = s

    return (a - 1, b), (a // 2, b), (a, b - 1), (a, b // 2)


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

for s in range(1, 1561651 + 1):
    print(s, play((10, s)))

# print(19, [s for s in range(11, 154) if any(play(t) in "V1" for t in moves((10, s)))])
# print(20, [s for s in range(11, 154) if play((10, s)) in "V2"])
# print(21, [s for s in range(11, 154) if play((10, s)) in "P2"])