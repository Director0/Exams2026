f = open("17_24200.txt")

nums = [int(x) for x in f]
sums = []
n2 = len([x for x in nums if x % 2 == 0])
gcnt = 0

for i in range(len(nums) - 1):
    if len(str(nums[i])) > 2 and len(str(nums[i + 1])) > 2:
        if (str(nums[i])[-3] == "0" or str(nums[i + 1])[-3] == "0") and ((nums[i] * nums[i + 1]) % n2 == 0):
            gcnt += 1
            sums.append(nums[i] + nums[i + 1])

print(gcnt)
print(abs(max(sums)))