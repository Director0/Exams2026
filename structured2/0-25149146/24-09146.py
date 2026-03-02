from itertools import *

s = open("24.txt").read()

lsc = set()

for i in product("ABCDEF", repeat=5):
    i1 = "".join(i)
    if i1.count("B") + i1.count("C") + i1.count("D") + i1.count("F") > i1.count("A") + i1.count("E"):
        lsc.add(i1)


for a in lsc:
    s = s.replace(a, "x")


print(s)

s = s.replace("A", " ").replace("B", " ").replace("C", " ").replace("D", " ").replace("E", " ").replace("F", " ").split()

print(s)

print(max(s, key=len))
print(len(max(s, key=len)))