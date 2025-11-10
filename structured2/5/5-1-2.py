# res = []
#
# for n in range(100, 1000):
#     l1 = "".join(str(x) for x in sorted([int(str(n)[0]) * int(str(n)[1]), int(str(n)[1]) * int(str(n)[2])]))
#     print(n, l1)
#     res.append((n, l1))
#
# for nl in res:
#     if nl[1] == "621":
#         print(nl)
#


for n in range(100, 1000):
    if "".join(str(x) for x in sorted([int(str(n)[0]) * int(str(n)[1]), int(str(n)[1]) * int(str(n)[2])])) == "621":
        print(n)
