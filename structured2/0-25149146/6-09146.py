from turtle import *

screensize(2500, 2500)
tracer(0)
scl = 20

lt(90)

# //

for i in range(40000):
    fd(15 * scl)
    rt(90)
    fd(22 * scl)
    rt(90)

up()

fd(6 * scl)
rt(90)
fd(7 * scl)
lt(90)

down()

for i in range(99999):
    fd(120 * scl)
    rt(90)
    fd(200 * scl)
    rt(90)


up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * scl, y * scl)
        dot(3, "red")


update()
done()
