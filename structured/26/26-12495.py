f = open("26_12495.txt")
# 10000 1021000 11111

ls = [int(s) for s in f]
km = 1021000
vol = 11111

ls.sort()
vm = 0
vk = 0
cnt = 0

for v in ls:
    if v > vk + vol:
        vk = vm
        cnt += 1

    if v > vm and v <= vk + vol:
        vm = v

    if vm + vol > km:
        cnt += 1
        d = vm
        break

print(d)
print(cnt)
exit()