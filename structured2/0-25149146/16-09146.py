def f(n):
    if n < 100:
        return 4 * n
    else:
        if n % 2 == 0:
            return 35 + f(n - 1)
        else:
            return 2 * f(n - 1)


sn = 1
print(str(6 * f(151)))

for x in str(6 * f(151)):
    sn *= int(x)


print(sn)