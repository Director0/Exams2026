# from turtle import *
#
# screensize(2500, 2500)
# tracer(0)
# scl = 20
# p = 5
#
# lt(90)
#
# #? /
#
# for i in range(4):
#     fd(3 * p * scl)
#     rt(90)
#
# up()
#
# fd(p * scl)
# rt(90)
# fd(p * scl)
#
# down()
#
# for i in range(4):
#     fd(p * scl)
#     lt(90)
#
# up()
# # //
#
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x * scl, y * scl)
#         dot(3, "red")
#
#
# done()

for x in range(1, 1000):
    if (3*x - 1)**2 - (x+1)**2 <= 10**6:
        print(x)