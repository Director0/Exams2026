from turtle import *

screensize(1000, 1000)
tracer(0)
scl = 30

lt(90)

# //

rt(225)

for i in range(6):
    fd(15 * scl)
    rt(60)
    fd(7 * scl)
    rt(120)

up()

# //

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * scl, y * scl)
        dot(3, "red")


done()