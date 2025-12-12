f = open("17.txt")

nums = [int(x) for x in f]
sums = []
maxcb = max(nums,) ** 3
cnt = 0

for i in range(len(nums) - 1):
    if ((sum(int(s) for s in nums[i]) % 5 == 0) and (sum(int(s) for s in nums[i + 1]) % 5 != 0)):
        print(0)