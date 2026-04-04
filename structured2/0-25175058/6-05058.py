from turtle import *

screensize(1000, 1000)
tracer(0)
scl = 20

lt(90)

# //

lt(40)

for i in range(5):
    rt(-95)
    fd(12 * scl)
    lt(45)
    fd(8 * scl)
    lt(40)


up()

# //

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * scl, y * scl)
        dot(3, "red")


done()