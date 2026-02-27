cnt = 0

def f(n):
    global cnt
    print('*')
    cnt += 1
    if n >= 1:
        print('*')
        cnt += 1
        f(n - 1)
        f(n // 2)

f(40)
print(cnt)