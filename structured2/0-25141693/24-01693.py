from re import *

s = open("24.txt").read()

pat = r"[+]7[(]987[)](?:[0-9]){3}-(?:[0-9]){2}-44"

d = findall(pat, s)

print(d)