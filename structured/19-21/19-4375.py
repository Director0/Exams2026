from functools import lru_cache

def moves(s, s_prev, s_prev1):
    if s_prev1 == "+1":
        return (s + 2, "+2", s_prev), (s * 2, "*2", s_prev)
    elif s_prev1 == "+2":
        return (s + 1, "+1", s_prev), (s * 2, "*2", s_prev)
    elif s_prev1 == "*2":
        return (s + 1, "+1", s_prev), (s + 2, "+2", s_prev)
    else:
        return (s + 1, "+1", s_prev), (s + 2, "+2", s_prev), (s * 2, "*2", s_prev)


@lru_cache(maxsize=None)
def play(s, s_prev, s_prev1):
    if s >= 29:
        return "P0"
    elif any(play(t, x, y) in "P0" for t, x, y in moves(s, s_prev, s_prev1)):
        return "V1"
    elif all(play(t, x, y) in "V1" for t, x, y in moves(s, s_prev, s_prev1)):
        return "P1"
    elif any(play(t, x, y) in "P1" for t, x, y in moves(s, s_prev, s_prev1)):
        return "V2"
    elif all(play(t, x, y) in "V1V2" for t, x, y in moves(s, s_prev, s_prev1)):
        return "P2"
    elif any(play(t, x, y) in "P1P2" for t, x, y in moves(s, s_prev, s_prev1)):
        return "V3"
    else:
        return "?"

for s in range(1, 30):
    print(s, play(s, "", ""))
# V2, P2, V3
# 19/ 12
# 20/ 10, 11
# 21/ 9
