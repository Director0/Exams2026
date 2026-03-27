s = open("24.txt").read()


curl = 1
eco = 0

for i in range(len(s) - 1):
    if s[i] == s[i + 1] and curl < 5:
        curl += 1
    else:
        if curl > 2:
            eco += curl - 2

        curl = 1

if curl > 2:
    eco += curl - 2

print(eco * 8)