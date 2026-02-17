from turtle import *

screensize(2500, 2500)
tracer(0)
scl = 20

lt(90)

# //

for i in range(5):
    fd(42 * scl)
    rt(270)
    fd(55 * scl)
    lt(90)

up()

fd(17 * scl)
rt(90)
fd(12 * scl)
lt(90)

down()

for i in range(14):
    fd(14 * scl)
    lt(90)
    fd(200 * scl)
    lt(90)

up()

# //

for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * scl, y * scl)
        dot(3, "red")

done()