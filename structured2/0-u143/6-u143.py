from turtle import *

screensize(10000, 10000)
tracer(0)
scl = 20

lt(90)

# //

for i in range(12):
    rt(90)
    fd(125 * scl)
    rt(90)
    fd(17 * scl)


up()

# //

for x in range(-20, 130):
    for y in range(-20, 130):
        goto(x * scl, y * scl)
        dot(3, "red")


done()
