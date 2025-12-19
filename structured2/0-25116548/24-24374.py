f = open("24_24374.txt").read()
f1 = f
# f = "H445KCHYZNEXXPWR2FRG9O567GZ9D5TZ765P4VNM98C2IP19JLVBU3TR0EKGC42VYT0SLUHFZVG8AK4FA770I3GFA3FHZ8OV4OL7EQY6RJB6AMAA58TWR8MQNWVRH8NQ606U09E8"

for n in "0123456789":
    f1 = f1.replace(n, " ")

f1 = f1.split()

lns = []

for a in f1:
    lns.append(len(a))

maxlen = -10**21
stp = ""
# print(lns, len(lns))

for i in range(len(lns) - 80):
    a1 = sum(lns[i:(i+80)])
    print(a1)

    if a1 > maxlen:
        maxlen, stp = a1, f1[i]


print(maxlen, f.index(stp))
print(f.index("SIDPWQ01K120ZJX"))

# 2576274 ans