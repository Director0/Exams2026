from turtle import *

screensize(2000, 2000)
tracer(0)
scl = 13



# //

for i in range(3):
    goto(xcor() + (90 * scl), ycor() + (90 * scl))
    goto(xcor() + (-60 * scl), ycor() + (0 * scl))
    goto(xcor() + (-30 * scl), ycor() + (-90 * scl))



# //

up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * scl, y * scl)
        dot(3, "red")


done()