from turtle import *

screensize(1000, 1000)
tracer(0)
scl = 20
cnv = getcanvas()

up()

# //

for i in range(27):
    fd(5 * scl)

    if cnv.find_overlapping(xcor(), ycor(), xcor(), ycor()):
        dot(5, "black")
    else:
        dot(10, "red")

    bk(3 * scl)

    if cnv.find_overlapping(xcor(), ycor(), xcor(), ycor()):
        dot(5, "black")
    else:
        dot(10, "red")

    bk(3 * scl)


done()