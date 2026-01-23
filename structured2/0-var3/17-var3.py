f = open("17.txt")

nums = [int(x) for x in f]
sumsq = []
min1 = min([x for x in nums if len(str(abs(x))) >= 2 and str(x)[-1] == str(x)[-2]])
cnt = 0

for i in range(len(nums) - 1):
    ls = [nums[i], nums[i + 1]]
    ls1 = [str(x) for x in ls]

    if ((ls1[0][-1] == ls1[1][-2]) or (ls1[1][-1] == ls1[0][-2])) and (len([x for x in ls if x % 13 == 0]) == 1) and ((ls[0]**2 + ls[1]**2) <= min1**2):
        sumsq.append((ls[0]**2 + ls[1]**2))


print(len(sumsq))
print(max(sumsq))