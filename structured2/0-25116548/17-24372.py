f = open("17_24372.txt")

nums = [int(x) for x in f]
sums = []
nums3 = [x for x in nums if x % 3 == 0 and x < 0]


for i in range(len(nums) - 1):
    if ((nums[i] >= 0 and nums[i + 1] < 0) or (nums[i] < 0 and nums[i + 1] >= 0)) and (abs(nums[i] - nums[i + 1]) % len(nums3) == 0):
        sums.append(nums[i] + nums[i + 1])

print(len(sums), max(sums))
