from turtle import *

screensize(10000, 10000)
tracer(0)
scl = 21

lt(90)

# //


for i in range(10):
    goto(xcor() + (3 * scl), ycor() + (-4 * scl))
    goto(xcor() + (-7 * scl), ycor() + (24 * scl))
    goto(xcor() + (12 * scl), ycor() + (5 * scl))


up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * scl, y * scl)
        dot(3, "red")


done()