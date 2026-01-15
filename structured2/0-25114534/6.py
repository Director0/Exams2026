from turtle import *

screensize(1000,1000)
tracer(0)
scl=20

lt(90)

for i in range(2):
    fd(6*scl)
    lt(270)
    bk(20*scl)
    rt(90)
up()
fd(3*scl)
rt(90)
bk(3*scl)
lt(90)
down()

for i in range(2):
    fd(15*scl)
    rt(90)
    fd(70*scl)
    rt(90)

up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*scl,y*scl)
        dot(3,"red")
done()
