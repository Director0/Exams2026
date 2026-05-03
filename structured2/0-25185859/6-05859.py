from turtle import *

screensize(1000, 1000)
tracer(0)
scl = 50

lt(90)
# //

for i in range(2):
    goto(xcor() + (6 * scl), ycor() + (2 * scl))
    goto(xcor() + (0 * scl), ycor() + (-2 * scl))

for i in range(3):
    goto(xcor() + (2 * scl), ycor() + (-1 * scl))
    goto(xcor() + (-2 * scl), ycor() + (-1 * scl))

for i in range(6):
    goto(xcor() + (-2 * scl), ycor() + (1 * scl))


up()

# //

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * scl, y * scl)
        dot(3, "red")


done()