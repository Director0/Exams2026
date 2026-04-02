f = open("17.txt")

nums = [int(x) for x in f]
sums = []
min99 = min([x for x in nums if x > 0 and len(str(abs(x))) >= 2 and str(abs(x))[-2:] == "99"])


for i in range(len(nums) - 2):
    ls = [nums[i], nums[i + 1], nums[i + 2]]

    if len([x for x in ls if len(str(abs(x))) == 3]) >= 2 and sum(ls) >= min99:
        sums.append(sum(ls))


print(len(sums))
print(min(sums))