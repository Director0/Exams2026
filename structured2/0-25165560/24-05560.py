s = open("24.txt").read()
s = "AAAAABBBCCDAAAAA"
s1 = s

for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    s = s.replace(f"{x}{x}{x}{x}{x}", f"5{x}")

for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    s = s.replace(f"{x}{x}{x}{x}", f"4{x}")

for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    s = s.replace(f"{x}{x}{x}", f"3{x}")

for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    s = s.replace(f"{x}{x}", f"2{x}")


print(len(s1))
print(len(s))

print(len(s1) - len(s))

