def f(n):
    if n <= 18:
        return n + 3
    elif n > 18 and n % 3 == 0:
        return (n // 3) * f(n // 3) + n - 12
    elif n > 18 and n % 3 != 0:
        return f(n - 1) + n**2 + 5

cnt = 0

for n in range(1, 1001):
    if all(x in "02468" for x in str(f(n))):
        cnt += 1
        print(n)


print(f"cnt: {cnt}")