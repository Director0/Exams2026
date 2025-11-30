from turtle import *

screensize(1000, 1000)
tracer(0)
scl = 20


lt(90)

for i in range(6):
    fd (7 * scl)
    rt (120 * scl)
up()

fd(3*scl)
rt(90 * scl)

down()

for i in range(8):
    fd(5 *scl)
    rt(90*scl)

# ///
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * scl, y * scl)
        dot(3, "red")

done()