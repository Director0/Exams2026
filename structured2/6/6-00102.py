from turtle import *
from functools import lru_cache

@lru_cache(maxsize=None)
def dots(canv):
    lcnt = 0

    for x in range(-50, 50):
        for y in range(-50, 50):
            info = canv.find_overlapping(x * scl, y * scl, x * scl, y * scl)

            if len(info) == 1 and info[0] == 5:
                lcnt += 1

    return lcnt



screensize(1000, 1000)
tracer(0)
scl = 20

gcnt = 0



for x in range(30000):
    begin_fill()

    for i in range(7):
        fd(x * scl)
        rt(90)
        fd(5 * scl)
        rt(90)
        fd(3 * scl)

    end_fill()

    cnv = getcanvas()

    if dots(cnv) < 100000:
        print(x)
    else:
        exit()



done()
