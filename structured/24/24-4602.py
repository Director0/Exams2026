s = open("24_4602.txt").read()

# s = "BODOBODODOBCODODBCABODDODODABABADOCOCADADABABADADAAAAAA"

s = s.replace("B", "*").replace("C", "*").replace("D", "*").replace("A", "?").replace("O", "?")
s = s.replace("*?", "%").replace("*", " ").replace("?", " ")


print(s)
print(len(max(s.split(), key=len)))