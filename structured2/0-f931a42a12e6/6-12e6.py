from turtle import *

screensize(2500, 2500)
tracer(0)
scl = 20

lt(90)

# //

fd(10 * scl)
down()

for i in range(6):
    fd(50 * scl)
    rt(90)
    fd(43 * scl)
    rt(90)

up()

fd(40 * scl)
rt(90)
fd(40 * scl)

down()

for i in range(9):
    fd(40 * scl)
    lt(90)
    fd(20 * scl)
    lt(90)

up()

# //

for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * scl, y * scl)
        dot(3, "red")


done()