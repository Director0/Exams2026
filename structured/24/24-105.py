s = open("24_105.txt").read()

#s = "LIAAAAAAFAILFAFFFFFFFILALAALLAFLILIFALALLIFFFAILFAILFAILFAILLLLLLLLLLLLLLLFAILILLAILALLFAIALIALLLLLLFFAILFAILFAILALAALFFIAFAILLLFAIL"

for c1 in "FAIL":
    for c2 in "FAIL":
        if c1 != c2:
            s = s.replace(c1 + c2, f"{c1} {c2}")


#z

print(len(max(s.split(), key=len)))
