def f(x):
    p = 5 <= x <= 54
    q = 50 <= x <= 93


    return ((not p) and q) <= (x > a)



for a in range(-1000, 10000):
    rg = [1 if (not f(x)) else 0 for x in range(-1000, 10000)]

    if sum(rg) == 20:
        print(a)
