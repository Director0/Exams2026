s = open("24_9845.txt").read()



s = s.replace("A", "*").replace("B", "*").replace("C", "*").replace("8", "?").replace("9", "?")
s = s.replace("**", "* *").replace("??", "? ?")
s = s.replace("**", "* *").replace("??", "? ?")


print(len(max(s.split(), key=len)))
