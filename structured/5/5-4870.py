from itertools import permutations

for n in range(100, 1000):
    r1 = [int(x[0] + x[1]) for x in permutations(str(n), r = 2) if x[0] != "0"]

    n1 = max(r1)
    n2 = min(r1)

    n3 = n1 - n2

    if n3 == 5:
        print(n, n3)
        break

