from functools import lru_cache

def moves(s):
    a, b = s

    if a > 1 and b > 1:
        return (a - 1, b), (a, b - 1), ((a + 1) // 2, b), (a, (b + 1) // 2)
    elif a == 1:
        return (a - 1, b), (a, b - 1), (a, (b + 1) // 2)
    elif a == 0:
        return (a, b - 1), (a, (b + 1) // 2)
    elif b == 1:
        return (a - 1, b), (a, b - 1), ((a + 1) // 2, b)
    elif b == 0:
        return (a - 1, b), ((a + 1) // 2, b)

@lru_cache(maxsize=None)
def play(s):
    if sum(s) < 10:
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

for s in range(20, 200):
    print(s, play(10, s))

print(19, [s for s in range(20, 200) if play(10, s) in "P1"])
print(20, [s for s in range(20, 200) if play(10, s) in "V2"])
print(21, [s for s in range(20, 200) if play(10, s) in "P2"])