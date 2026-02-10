from functools import lru_cache
import sys

sys.setrecursionlimit(100000)

def moves(s):
    return s - 5, s // 3

@lru_cache(maxsize=None)
def play(s):
    if s < -2:
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

print(19, [s for s in range(1, 50) if play(s) in "P1"])
print(20, [s for s in range(1, 50) if play(s) in "V2"])
print(21, [s for s in range(1, 50) if play(s) in "P2"])