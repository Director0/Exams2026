def f(n):
    if n >= 3000:
        return n
    else:
        return n + x + f(n + 2)


for x in range(-50000, 50000):
    if f(2984) - f(2988) == 5916:
        print(x)