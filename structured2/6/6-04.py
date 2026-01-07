from turtle import *

screensize(5000, 5000)
tracer(0)
scl = 20

lt(90)

# ///

rt(315)

for i in range(7):
    fd(72 * scl)
    rt(45)
    fd(43 * scl)
    rt(135)

# ///
up()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * scl, y * scl)
        dot(3, "red")


done()