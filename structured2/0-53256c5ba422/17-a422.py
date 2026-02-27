f = open("17.txt")

nums = [int(x) for x in f]
sums = []
min25 = min([x for x in nums if abs(x) % 2025 == 0])


for i in range(len(nums) - 2):
    ls = [nums[i], nums[i + 1], nums[i + 2]]

    if any(x % min25 == 0 for x in ls) and len(str(abs(sum(ls)))) == 6:
        sums.append(sum(ls))


print(len(sums))
print(max(sums))