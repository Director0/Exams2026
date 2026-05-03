f = open("17_29349.txt")

nums = [int(x) for x in f]
sums = []
min123 = min([x for x in nums if x > 0 and abs(x) % 123 == 0])


for i in range(len(nums) - 2):
    ls = [nums[i], nums[i + 1]]

    if sum(ls) < min123:
        sums.append(sum(ls))


print(len(sums))
print(abs(max(sums)))