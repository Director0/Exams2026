f = open("17.txt")

nums = [int(x) for x in f]
sums = []
sums1 = []


for i in range(len(nums) - 1):
    ls = [nums[i], nums[i + 1]]
    b = [x for x in ls if x % 80 == 17]

    if len(b) == 1 and all(x % 7 == 0 for x in ls):
        sums.append(sum(ls))
        sums1 += b

print(len(sums))
print(sum(sums1))