n = 7 ** 202 + 49 ** 102 - 7 ** 20

cnt = 0

while n != 0:
    if n % 7 == 6:
        cnt += 1

    n //= 7

print(cnt)