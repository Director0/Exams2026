from turtle import *

screensize(10000, 10000)
tracer(0)
scl = 50

lt(90)

# //
up()
goto(-3 * scl, -4 * scl)
down()

rt(30)

for i in range(10):
    fd(14 * scl)
    rt(120)


up()
# //


for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * scl, y * scl)
        if x < 0 and y < 0:
            dot(4, "green")
        else:
            dot(3, "red")


done()
