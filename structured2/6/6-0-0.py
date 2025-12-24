from turtle import *

screensize(2502,2502)
tracer(0)
scl = 20

lt(90)


for i in range(6):
     fd(33 * scl)
     rt(90)
     fd(20 * scl)
     rt(90)
up()

fd(3 * scl)
rt(90)
fd(9 * scl)
lt(90)
down()

for i in range(6):
    fd(24 * scl)
    rt(90)
    fd(25 * scl)
    rt(90)

up()
for x in range(-50,50):
    for y in range(-50, 50):
        goto(x * scl,y * scl)
        dot(3,"red")

done()