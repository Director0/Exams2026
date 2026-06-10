f = open("9_08951.txt")

# def collide(dot1, dot2):


for s in f:
    ls = list(map(int, s.split()))

    cdot1 = [ls[0], ls[1]]
    cdot2 = [ls[2], ls[3]]