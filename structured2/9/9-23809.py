f = open("9_23809.txt")

cnt = 0

for s in f:
    nums3 = [x for x in s if s.count(x) == 3]
    nums1 = [x for x in s if s.count(x) == 1]

    if len(nums3) == 3 and nums1 != None and len(nums1) == 1:
        nums3 = [int(x) for x in nums3]
        if (sum(nums3) / len(nums3)) >= int(nums1[0]):
            cnt += 1


print(cnt)
