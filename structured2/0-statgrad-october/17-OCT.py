f = open("17.txt")

nums = [int(x) for x in f]
sums = []
m4 = max([x for x in nums if x < 0 and len(str(abs(x))) == 4 and x % 9 == 0])
cnt = 0

for i in range(len(nums) - 1):
    if ((nums[i] < 0 and nums[i + 1] >= 0) or (nums[i] >= 0 and nums[i + 1] < 0)) and ((nums[i] + nums[i + 1]) > m4):
        cnt += 1
        sums.append(nums[i] ** 2 + nums[i + 1] ** 2)

print(cnt)
print(min(sums))

