f = open("17_24074.txt")

nums = [int(x) for x in f]
sums = []
min9 = min([x for x in nums if len(str(abs(x))) == 3 and abs(x) % 10 == 9])


for i in range(len(nums) - 1):
    ls = [nums[i], nums[i + 1]]

    if len([x for x in ls if len(str(abs(x))) == 2]) > 0 and sum(ls) % min9 == 0:
        sums.append(sum(ls))


print(len(sums))
print(max(sums))