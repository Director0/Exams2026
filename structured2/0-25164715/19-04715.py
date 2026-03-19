from functools import lru_cache


def moves(s):
    return s + 2, s * 3


@lru_cache(maxsize=None)
def play(s):  # ваня
    if 36 <= s <= 85:
        return "P0"
    elif s > 85:
        return "L0"
    elif any(play(t) == "P0" for t in moves(s)):
        return "V1"
    elif all(play(t) == "V1" or play(t) == "L0"  for t in moves(s)):
        return "P1"
    elif any(play(t) == "P1" for t in moves(s)):
        return "V2"
    elif all(play(t) == "V1" or play(t) == "V2" or play(t) == "L0" for t in moves(s)):
        return "P2"
    elif any(play(t) in "P1P2" for t in moves(s)):
        return "V3"
    elif all(play(t) in "V1V2V3L0" for t in moves(s)):
        return "P3"
    elif any(play(t) in "P1P2P3" for t in moves(s)):
        return "V4"
    elif all(play(t) in ["V1V2V3V4", "L0"] for t in moves(s)):
        return "P4"

    else:
        return "?"


print(play(6))
print(play(10))


