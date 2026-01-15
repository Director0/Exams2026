print("m e o w F")
for m in range(2):
    for e in range(2):
        for o in range(2):
            for w in range(2):
                F = (m<=e) or (o==e) and w
                if F==0:
                    print(m,e,o,w,F*1)