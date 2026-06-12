from turtle import *

screensize(10000, 10000)
tracer(0)
scl = 20

lt(90)
# //

fd(25 * scl)
rt(45)
fd(50 * scl)

up()

bk(50 * scl)
rt(45)
fd(15 * scl)
lt(90)
fd(30 * scl)

down()

rt(180)
fd(60 * scl)
bk(5 * scl)
rt(90)
fd(31 * scl)

# //
up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * scl, y * scl)
        dot(3, "red")


done()