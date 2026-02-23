from turtle import *

screensize(1000, 1000)
tracer(0)
scl = 20

lt(90)

# //

for i in range(2):
    fd(13 * scl)
    rt(90)
    fd(20 * scl)
    rt(90)

up()

fd(8 * scl)
rt(90)
bk(3 * scl)
lt(90)

down()

for i in range(2):
    fd(16 * scl)
    rt(90)
    fd(8 * scl)
    rt(90)

up()

# //

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * scl, y * scl)
        dot(3, "red")


done()