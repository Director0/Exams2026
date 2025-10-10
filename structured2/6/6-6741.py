from turtle import *

screensize(1000, 1000)
tracer(0)
scl = 20

lt(90)

# ///

for i in range(4):
    fd(10 * scl)
    rt(270)

up()

fd(3 * scl)
rt(270)
fd(5 * scl)
rt(90)

down()

for i in range(2):
    fd(10 * scl)
    rt(270)
    fd(12 * scl)
    rt(270)

# ///
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * scl, y * scl)
        dot(3, "red")


done()