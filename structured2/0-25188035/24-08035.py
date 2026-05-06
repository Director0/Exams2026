s = open("24.txt").read()

s = s.replace("XYZ", "XY YZ").split()

print(max(s, key=len))
print(len(max(s, key=len)))