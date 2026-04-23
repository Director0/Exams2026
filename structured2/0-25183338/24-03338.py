s = open("24.txt").read()


for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
    s = s.replace(f"{x}{x}", f"{x} {x}")
    s = s.replace(f"{x}{x}", f"{x} {x}")
    s = s.replace(f"{x}{x}", f"{x} {x}")
    s = s.replace(f"{x}{x}", f"{x} {x}")
    s = s.replace(f"{x}{x}", f"{x} {x}")


s = s.split()
print(sorted(s, key=len))
print(max(s, key=len))
print(len(max(s, key=len)))