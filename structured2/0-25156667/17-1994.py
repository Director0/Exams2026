f = open("17_1994.txt")

nums = [int(x) for x in f]
mlps = []


for i in range(len(nums) - 1):
    ls = [nums[i], nums[i + 1]]
    ml1 = 1

    for x in ls:
        ml1 *= x

    if (ml1 > 0) and (abs(sum(ls)) % 7 == 0):
        mlps.append(ml1)

print(len(mlps))
print(min(mlps))
