f = open("17_2937.txt")

nums = [int(x) for x in f]
sums = []
max11 = max([x for x in nums if abs(x) % 11 == 0])


for i in range(len(nums) - 1):
    ls = [nums[i], nums[i + 1]]

    if any(x % 11 == 0 for x in ls) and (sum(ls) <= max11):
        sums.append(sum(ls))


print(len(sums), max(sums))