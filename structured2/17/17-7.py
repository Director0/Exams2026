f = open("17_24200.txt")
A=[int(x) for x in f]
f.close()

A21=[x for x in A if len(str(abs(x)))>=2 and str(x)[-1]==str(x)[-2]]
A2=[x for x in A21 if x%2==0]
print(len(A21),max(A2))


