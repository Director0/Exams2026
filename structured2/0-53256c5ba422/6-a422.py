from turtle import *

screensize(1000, 1000)
tracer(0)
scl = 60

lt(90)

# //

for i in range(42):
    rt(60)
    fd(7 * scl)
    rt(60)


up()

# //

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * scl, y * scl)
        dot(3, "red")

done()