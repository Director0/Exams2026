from turtle import *

screensize(2000, 2000)
tracer(0)
scl = 50

lt(90)
# //

for i in range(5):
    fd(16 * scl)
    rt(120)


up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * scl, y * scl)
        dot(3, "red")

done()