from turtle import *

screensize(2500, 2500)
tracer(0)
scl = 20
x = 27

lt(90)
# //

for i in range(4):
    fd(x * scl)
    rt(90)
    fd(48 * scl)
    rt(90)


up()

fd(27 * scl)
rt(90)
fd(24 * scl)
lt(90)

down()

for i in range(4):
    fd(29 * scl)
    rt(90)
    bk(18 * scl)
    rt(90)

up()

# //
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * scl, y * scl)
        dot(3, "red")


done()
