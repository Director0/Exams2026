f = open("26 (4).txt")

blocks = [int(x) for x in f]
hses = 0


while blocks:
    skips = []
    b1 = blocks[0]
    bprev = b1
    hght = 1

    hses += 1



    for i in range(1, len(blocks)):
        if blocks[i] < bprev:
            if hght + 1 <= b1 // 2:
                hght += 1
                bprev = blocks[i]
            else:
                break
        else:
            skips.append(blocks[i])

    print(skips)

    if len(blocks) > 1:
        blocks = skips + blocks[i:]
    else:
        break

    print(blocks)


print(hses)
print(b1)
