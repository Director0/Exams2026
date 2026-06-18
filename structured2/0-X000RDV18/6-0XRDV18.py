from turtle import *

screensize(2500, 2500)
tracer(0)
scl = 20

# //

for i in range(2):
    fd(14 * scl)
    lt(270)
    bk(12 * scl)
    rt(90)

up()

fd(9 * scl)
rt(90)
bk(7 * scl)
lt(90)

down()

for i in range(2):
    fd(13 * scl)
    rt(90)
    fd(6 * scl)
    rt(90)


up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * scl, y * scl)
        dot(3, "red")


done()