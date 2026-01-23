from turtle import *
tracer(0)
pd()
right(90)
k = 10
screensize(2000,2000)
left(90)
for i in range(6):
    fd(73*k)
    left(180)
    bk(10*k)
    right(90)
    fd(80*k)
    left(90)

pu()
fd(30*k)
left(90)
fd(9*k)
right(90)
pd()
for i in range(6):
    fd(24*k)
    right(90)
    fd(25*k)
    right(90)
pu()
for x in range(-10,70):
    for y in range(-10,20):
        goto(x*k, y*k)
        dot(3,'red')

update()
#Ответ 30
