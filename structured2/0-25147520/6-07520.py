from turtle import *

screensize(1000, 1000)
tracer(0)
scl = 20

lt(90)

# //

for i in range(4):
    fd(16 * scl)
    rt(90)
    fd(18 * scl)
    rt(90)

up()

rt(90)
fd(10 * scl)
lt(90)
fd(10 * scl)

down()

for i in range(4):
    fd(15 * scl)
    rt(90)

up()

fd(1 * scl)
lt(90)
fd(1 * scl)
rt(90)

down()

for i in range(7):
    fd(12 * scl)
    rt(90)


# //
up()

for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * scl, y * scl)
        dot(3, "red")

done()