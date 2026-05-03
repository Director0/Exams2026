from turtle import *

screensize(3500, 3500)
tracer(0)
scl = 17

lt(90)

# //

for i in range(6):
    fd(71 * scl)
    rt(90)
    fd(73 * scl)
    rt(90)

up()

fd(18 * scl)
rt(90)
fd(22 * scl)
lt(90)

down()

for i in range(6):
    fd(45 * scl)
    rt(90)
    fd(58 * scl)
    rt(90)


up()

# //

for x in range(-40, 90):
    for y in range(-40, 90):
        goto(x * scl, y * scl)
        dot(3, "red")



done()