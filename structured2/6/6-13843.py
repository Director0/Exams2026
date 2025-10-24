from turtle import *

screensize(1000, 1000)
tracer(0)
scl = 20

lt(90)

for i in range(5):
    rt(45)
    fd(10 * scl)
    rt(45)

for i in range(6):
    fd(20 * scl)
    rt(90)

up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * scl, y * scl)
        dot(3, "red")


done()

