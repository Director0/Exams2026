
def prim(n):
    ans = []
    d = 2

    while n > 1 and d ** 2 <= n:
        if n % d == 0:
            ans.append(d)
            n //= d
        else:
            d += 1

    if n != 1:
        ans.append(n)

    return ans


for n in range(987654321, 1, -1):
    slm = prim(n)

    if len(slm) == 13 and "1" in str(sum(slm)):
        print(n, max(slm))


# // 2
# def prim(n):
#     ans = []
#     d = 2
#
#     while d ** 2 <= n:
#         if n % d == 0:
#             ans.append(d)
#             n //= d
#         else:
#             d += 1
#
#     ans.append(n)
#
#     return ans
#
#
# for n in range(987654321, 1, -1):
#     slm = prim(n)
#
#     if len(slm) == 13 and "1" in str(sum(slm)):
#         print(n, max(slm))