# def cnt4(num, n):
#     cnt = 0
#
#     while num != 0:
#         if num % n == 4:
#             cnt += 1
#
#         num //= n
#
#     return cnt
#
# res = []
#
# for x in range(2, 2026):
#     n = 2 ** 2025 + 5 ** 200 - x
#
#     res.append([x, cnt4(n, 5)])
#
# res.sort(key=lambda x:x[1], reverse=True)
# print(res)
# print(min(res))

m=[]
for x in range(2,2026):
    n=5**2025+5**200-x
    k=0
    while n!=0:
        if n%5==4:
            k=k+1
        n=n//5
    m.append(k)
print(max(m),m.index(max(m))+2)