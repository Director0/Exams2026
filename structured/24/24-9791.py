s = open("24_9791.txt").read()



for s1 in "GHIJKLMNOPQRSTUVWXYZ":
    s = s.replace(s1, " ")



print(s)
print(len(max(s.split(), key=len)))