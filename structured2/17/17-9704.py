f = open("17_9704.txt")

nums = [int(x) for x in f]
sums = []
cnt = 0

for i in range(len(nums) - 1):
    if (len(str(nums[i])) == 2 and  len(str(nums[i + 1])) != 2) or (len(str(nums[i + 1])) == 2 and len(str(nums[i])) != 2):
        sums.append(nums[i] + nums[i + 1])


for i in range(len(nums) - 1):
    if i > max(sums):
        cnt += 1

print(cnt)