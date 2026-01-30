print("x y z w F")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F=not(w<=(z==y)) and (x<=z)
                if F==1:
                    print(x,y,z,w,F*1)