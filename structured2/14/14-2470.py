cnt = 0

for n in range(125, 243 + 1):
    if n % 16 == 13:
        cnt += 1


print(cnt)
