from functools import lru_cache

def dvs(n):
    divs = set()

    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            divs.add(d)
            divs.add(n // d)

    return divs or {0}


fl = False

def moves(s):
    global fl

    mvs = []

    mvs.append(s + 1)
    mvs.append(s + 4)

    if fl == False:
        mvs.append(s + sum(dvs(s)))
        fl = True

    return mvs


@lru_cache(maxsize=None)
def play(s):
    global fl

    if s >= 41:
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


print(19, [s for s in range(1, 43) if any(play(t) in "V1" for t in moves(s))])
print(20, [s for s in range(1, 43) if play(s) in "V2"])
print(21, [s for s in range(1, 43) if play(s) in "V1"])