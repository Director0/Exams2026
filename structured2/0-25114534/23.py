def f(x,y):
    if x < y or x %6==0:
        return 0
    elif x == y:
        return 1
    else:
        return (f(x-1,y)+ f(x//3,y)+ f(x//4,y))
print(f(100,33)*f(33,1))