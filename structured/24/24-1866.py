s = open("24_1866.txt").read()



s = s.replace("ad", "a d").replace("da", "d a")

print(len(max(s.split(), key=len)))