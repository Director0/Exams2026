from functools import lru_cache

def moves(s, s_prev):
    if s_prev == "+3":
        return (s + 6, "+6"), (s * 2, "*2")
    elif s_prev == "+6":
        return (s + 3, "+3"), (s * 2, "*2")
    elif s_prev == "*2":
        return (s + 3, "+3"), (s + 6, "+6")
    else:
        return (s + 3, "+3"), (s + 6, "+6"), (s * 2, "*2")

@lru_cache(maxsize=None)
def play(s, s_prev):
    if s > 40:
        return "P0"
    elif any(play(t, sn) in "P0" for t, sn in moves(s, s_prev)):
        return "V1"
    elif all(play(t, sn) in "V1" for t, sn in moves(s, s_prev)):
        return "P1"
    elif any(play(t, sn) in "P1" for t, sn in moves(s, s_prev)):
        return "V2"
    elif all(play(t, sn) in "V1V2" for t, sn in moves(s, s_prev)):
        return "P2"
    else:
        return "?"

print(19, [s for s in range(1, 37) if play(s, "") in "P1"])
print(20, [s for s in range(1, 37) if play(s, "") in "V2"])
print(21, [s for s in range(1, 37) if play(s, "") in "P2"])