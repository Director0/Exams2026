from turtle import *

x0 = xcor()
y0 = ycor()

for k in range(9):
    fd(18)
    rt(72)

x1 = xcor()
y1 = ycor()

print(((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5)