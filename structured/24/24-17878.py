s = open("24_17878.txt").read()



s = s.replace("6", "1").replace("7", "1").replace("8", "1").replace("9", "1")
s = s.replace("-", "*").replace("**", " ").replace("*01", "*0 1").replace("*00", "*0 0").replace(" *", " ").replace(" *", " ")
s = s.replace(" 01", " 0 1").replace(" 00", " 0 0")

print(s)
print(len(max(s.split(), key=len)))