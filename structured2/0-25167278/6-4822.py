from turtle import *

screensize(5000, 5000)
tracer(0)
scl = 15


# //
down()

for i in range(7):
    goto((xcor() + 6 * scl), (ycor() - 9 * scl))
    dot(5, "black")
    goto((xcor() - 6 * scl), (ycor() + 2 * scl))
    dot(5, "black")
    goto((xcor() + 12 * scl), (ycor() + 3 * scl))
    dot(5, "black")


up()

# //

for x in range(-50, 200):
    for y in range(-50, 50):
        goto(x * scl, y * scl)
        dot(3, "red")


done()