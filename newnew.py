for n in range(1000, 10000):
    d1, d2, d3, d4 = [int(x) for x in str(n)]
    nums = sorted([d1 * d2, d1 * d3, d1 * d4])
    res = str(nums[-2]) + str(nums[-1])

    if res == "5472":
        print(n)
        break