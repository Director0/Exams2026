from turtle import *

screensize(5000, 5000)
tracer(0)
scl = 21
x = 0
y = 0

lt(90)

def move(a, b):
    global x, y, scl

    x, y = x + a, y + b

    goto(x * scl, y * scl)


# //

up()

move(5, 5)

down()

for i in range(20):
    move(-5, -5)
    move(0, 5)

move(0, -5)

for i in range(20):
    move(5, 0)


up()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * scl, y * scl)
        dot(3, "red")


done()