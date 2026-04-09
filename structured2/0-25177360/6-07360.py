from turtle import *

screensize(1000, 1000)
tracer(0)
scl = 20

# //

up()

bk(3 * scl)
rt(90)
bk(15 * scl)
lt(90)

down()

for i in range(2):
    fd(10 * scl)
    rt(90)
    fd(18 * scl)
    rt(90)

up()

fd(5 * scl)
rt(90)
fd(7 * scl)
lt(90)

down()

for i in range(2):
    fd(10 * scl)
    rt(90)
    fd(7 * scl)
    rt(90)

up()

# //

for x in range(0, 50):
    for y in range(0, 50):
        goto(x * scl, y * scl)
        dot(3, "red")


done()


