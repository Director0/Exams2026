f = open("17_24200.txt")

nums = [int(x) for x in f]

sums = []
cnt2 = len([x for x in nums if abs(x) % 2 == 0])