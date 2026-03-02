from re import *

s = open("2c9d676d-2278-41b3-b382-255884b792da_24.6.txt").read()

pat = r"(?:(?:AN|NT)+|(?:NT|AN)+)+"

d = findall(pat, s)

print(max(d, key=len))
print(len(max(d, key=len)))