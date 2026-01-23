from functools import lru_cache

f = open("17_1.txt")

nums = [int(x) for x in f]
prs = []
max17 = max([x for x in nums if x % 100 == 17])
cnt = 0

@lru_cache(maxsize=None)
def div_n(n):
    divs = set()

    for i in range(2, int(abs(n**0.5)) + 1):
        if abs(n) % i == 0:
            divs.add(abs(n))
            divs.add(abs(n // i))

    return divs or 0


for i in range(len(nums) - 1):
    ls = [nums[i], nums[i + 1]]

    if (not ((div_n(ls[0]) == 0 and div_n(ls[1]) == 0) or (div_n(ls[0]) != 0 and div_n(ls[1]) != 0))) and (sum(ls) % max17 == 0):
        prs.append(ls[0] * ls[1])

print(prs)
print(len(prs), max(prs))