f = open("17.4_O4Ymomn.txt")

nums = [int(x) for x in f]
sums = []


for i in range(len(nums) - 1):
    ls = [nums[i], nums[i + 1]]

    if any(x > 500 for x in ls):
        sums.append(ls[0]**2 + ls[1]**2)


print(len(sums))
print(max(sums))