f = open("17 (1).txt")

nums = [int(x) for x in f]
sums = []
sum1 = sum(nums)


for i in range(len(nums) - 2):
    ls = [nums[i], nums[i + 1], nums[i + 2]]
    lsi = [i + 1, i + 2, i + 3]

    if str(sum(lsi))[-1] == str(sum1)[-1]:
        sums.append(abs(sum(ls) - sum(lsi)))


print(len(sums))
print(max(sums))