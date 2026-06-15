f = open("17_27629.txt")

nums = [int(x) for x in f]
sums = []
max43 = max([x for x in nums if len(str(abs(x))) == 4 and abs(x) % 100 == 43])


for i in range(len(nums) - 2):
    ls = [nums[i], nums[i + 1]]

    if any(len(str(abs(x))) == 4 for x in ls) and sum(ls)**2 < max43**2:
        sums.append(sum(ls)**2)


print(len(sums))
print(max(sums))