f = open("17_9840.txt")

nums = [int(x) for x in f]
sums = []
max39 = max([x for x in nums if len(str(abs(x))) == 4 and abs(x) % 100 == 39])

for i in range(len(nums) - 1):
    ls = [nums[i], nums[i + 1]]

    if len([x for x in ls if len(str(abs(x))) == 4]) == 1 and sum(ls)**2 <= max39**2:
        sums.append(sum(ls))


print(len(sums))
print(max(sums))