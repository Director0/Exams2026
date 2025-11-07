f = open("17_23949.txt")

nums = [int(x) for x in f]
sums = []


for i in range(len(nums) - 2):
    cnt = 0
    cnt1 = 0
    lst = [nums[i], nums[i + 1], nums[i + 2]]

    for i1 in lst:
        if str(i1)[0] == str(i1)[-1]:
            cnt += 1

        if len(str(i1)) == 5 and str(i1)[1] == "7":
            cnt1 += 1

    if cnt == 1 and cnt1 == 2:
        sums.append(max(lst))



print(len(sums))
print(sum(sums))
