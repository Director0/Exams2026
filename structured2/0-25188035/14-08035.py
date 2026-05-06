n = (25**500 * (4 * 6 + 1)**5**(3+1) + 7) // 128

cnt = 0

while n != 0:
    if n % 5 == 4:
        cnt += 1

    n //= 5


print(cnt)
