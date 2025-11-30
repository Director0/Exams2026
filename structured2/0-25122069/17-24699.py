f = open("17_24699.txt")

nums = [int(x) for x in f]
n_max = max([x for x in nums if len(str(x)) == 2])
sums = []

for i in range(len(nums) - 1):
    n1 = [len(str(abs(nums[i]))), len(str(abs(nums[i + 1])))]
    if n1.count(2) == 1 and (nums[i] + nums[i + 1]) % n_max == 0:
        sums.append(nums[i] + nums[i + 1])

print(len(sums))
print(max(sums))
