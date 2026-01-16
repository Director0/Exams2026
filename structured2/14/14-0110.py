def cnt0(num, n):
    cnt = 0

    while num != 0:
        if num % n == 0:
            cnt += 1

        num //= n

    return cnt

res = []

for x in range(0, 32001):
    n = 75 ** 314 + 75 ** 118 - x

    res.append(cnt0(n, 75))

print(res)
print(min(res))

