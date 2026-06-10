def f(x, y):
    return (x < a) and (y < 3*a) or (2*x + y > 128)

ls = []

for a in range(1, 1000):
    if all(f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
        ls.append(a)
        print(a)


print(f"min: {min(ls)}")