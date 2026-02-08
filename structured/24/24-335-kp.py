from re import *

s = open("24-335.txt").read()

a = r"[1-9][0-9]*[12346789]|[12346789]"
b = r"[1-9][0-9]*[05]|[5]"
pat = rf"(?:\((?:{a})[+-](?:{b})\))+"

d = findall(pat, s)

print(max(d, key=len))
print(len(max(d, key=len)))