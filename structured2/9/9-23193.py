f = open("9_23193.txt")

num = 0
nums = []

for s in f:
    num += 1

    s1 = list(map(int, s.split()))
    lst = []
    num1 = 0
    nums1 = []

    for n in s1:
        lst.append(s1.count(n))

        if s1.count(n) == 3:
            num1 = n

        if s1.count(n) == 1:
            nums1.append(n)

    if sum(lst) == 12 and len(nums1) != 0 and num1 > sum(nums1) / len(nums1):
        nums.append(num)

print(max(nums))