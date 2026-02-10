cnt = 0

for n in range(2, 10000):
    n1 = f"{n:b}"

    n1 = n1 + n1[-2]
    n1 = n1 + n1[1]

    r = int(n1, 2)

    if 150 <= r <= 250:
        cnt += 1
        print(r)

print("cnt:", cnt)