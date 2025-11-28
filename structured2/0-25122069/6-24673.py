from turtle import *

screensize(1000, 1000)
tracer(0)
scl = 20

lt(90)

# ///

for i in range(4):
    fd(20 * scl)
    rt(90)

up()

rt(90)
fd(3 * scl)
lt(90)

down()

for i in range(4):
    lt(90)
    fd(14 * scl)

up()

fd(20 * scl)

down()

for i in range(4):
    fd(6 * scl)
    rt(90)

rt(90)

up()

fd(4 * scl)
lt(90)
fd(4 * scl)

down()

for i in range(2):
    lt(90)
    fd(6 * scl)
    lt(90)
    fd(28 * scl)



# ///
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * scl, y * scl)
        dot(3, "red")


done()