from turtle import *

screensize(2500, 2500)
tracer(0)
scl = 20

lt(90)

for i in range(8):
    fd(22 * scl)
    rt(90)
    fd(33 * scl)
    rt(90)

up()

bk(8 * scl)
rt(90)
fd(11 * scl)
lt(90)
down()

for i in range(8):
    fd(73 * scl)
    rt(90)
    fd(62 * scl)
    rt(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * scl, y * scl)
        dot(3, "red")


done()
