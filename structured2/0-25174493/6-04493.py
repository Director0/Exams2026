from turtle import *

screensize(5000, 5000)
tracer(0)
scl = 7


lt(90)
up()
goto(10 * scl, 15 * scl)
down()

# //

for i in range(15):
    for i1 in range(20):
        fd(40 * scl)
        lt(90)

    lt(90)


up()

# //

for x in range(1, 50):
    for y in range(1, 50):
        goto(x * scl, y * scl)
        dot(3, "red")


done()

