f = open("24.txt").read()

#f = "35+51714**322646912265482+64+54*7**95617929+37367+8815384*588+73*11+36261+1*48*56*5971+6+*3796388*395*+*1745633837765+99"

for s in "0123456789":
    f = f.replace(s, "x")

#print(f)
f = f.replace("+", "$").replace("*", "$")

f = f.replace("$$", " ")


f = f.replace(" $", " ").replace("$ ", " ")

#print(f)
f = f.split()
ml = 0

for x in f:
    x = x.split("$")

    for i in range(len(x)):
        l = x[i:i+40]
        l1 = "?".join(l)
        ml = max(ml, len(l1))

print(ml)
#print(f)
print("\n")
print("RESSS: ", max(f, key=len))
print(len(max([x for x in f if x.count("$") < 40], key=len)))