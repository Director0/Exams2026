f = open("17.txt")

nums = [int(x) for x in f]
sums = []


for i in range(len(nums) - 1):
    ls = [nums[i], nums[i + 1]]

    if abs(ls[0] * ls[1]) % 2 != 0 and (sum(ls)/len(ls)) % 7 == 0:
        sums.append(sum(ls)/len(ls))


print(len(sums))
print(min(sums))