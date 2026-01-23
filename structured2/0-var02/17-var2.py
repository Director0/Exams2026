f = open("17.txt")

nums = [int(x) for x in f]
sums = []
min1 = min([x for x in nums if x > 0 and len(str(abs(x))) == 4 and x % 10 == 6])
cnt = 0

for i in range(len(nums) - 2):
    ls = [nums[i], nums[i + 1], nums[i + 2]]

    if (len([x for x in ls if len(str(abs(x))) == 4]) == 1) and (sum(ls) <= min1):
        sums.append(sum(ls))

print(len(ls))
print(sum(ls))