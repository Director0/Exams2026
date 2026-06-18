for a in range(1, 1000):
    b = range(50, 71)
    F = 1
    for x in range(1, 1000):
        F = F and ( (x % a == 0) or (x % 23 == 0) <= (x not in b) )
    if F == 1:
        print(a)  # ans 69