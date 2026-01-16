from itertools import *

alb = "0123456789ABCDEF"
cnt = 0


for n in product(alb, repeat=4):
    n1 = "".join(n)

    if (n1.count("3") == 1) and n1[0] != n1[1] and n1[1] != n1[2] and n1[2] != n1[3] and (n1[0] != "0"): #NOT [0???]
        print(n1)
        cnt += 1

print(cnt)