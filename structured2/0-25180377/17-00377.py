f = open("17.txt")

nums = [int(x) for x in f]
sums = []


for i in range(len(nums) - 1):
    ls = [nums[i], nums[i + 1]]

    if abs(sum(ls)) % 3 == 0 and abs(sum(ls)) % 6 != 0 and str(abs(ls[0] * ls[1]))[-1] == "8":
        sums.append(sum(ls))



print(len(sums))
print(max(sums))