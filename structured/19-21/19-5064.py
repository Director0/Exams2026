from functools import lru_cache

def moves(s):
    return [x for x in [s + 1, s + 2, s * 2] if x % 3 != 0]

@lru_cache(maxsize=None)
def play(s):
    if s >= 151:
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

for s in range(1, 151 + 1):
    print(s, play(s))


print(19, [s for s in range(1, 152) if play(s) in "P1" and s % 3 != 0])
print(20, [s for s in range(1, 152) if play(s) in "V2" and s % 3 != 0])
print(21, [s for s in range(1, 152) if play(s) in "P2" and s % 3 != 0])