from turtle import *

screensize(1000, 1000)
tracer(0)
scl = 20

lt(90)

for i in range(4):
    for i in range(3):
        fd(2 * scl)
        rt(270)

    fd(5 * scl)

up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * scl, y* scl)
        dot(2, "red")
done()