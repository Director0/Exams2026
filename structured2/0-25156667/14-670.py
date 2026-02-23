n = 5 * 36**7 + 6**10 - 36

cnt = 0

while n != 0:
    if n % 6 == 5:
        cnt += 1

    n //= 6

print(cnt)