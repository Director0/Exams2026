f = open("17.txt")

nums = [int(x) for x in f]
sums = []
cnt = 0

for i in range(len(nums) - 2):
