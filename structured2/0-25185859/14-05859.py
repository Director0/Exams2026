
n = 3 * 5**1984 - 7 * 25**777 - 11 * 125**666 - 404
cnt = 0
print(n)

while n != 0:
    if n % 5 == 2:
        cnt += 1

    n //= 5


print(cnt)