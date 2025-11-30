s = open("24_17563.txt").read()

s = s.replace("-", "*").replace("**", " ").replace("*0", " ").replace(" 0", " ").replace(" *", " ").replace(" *", " ")



print(len(max(s.split(), key=len)))