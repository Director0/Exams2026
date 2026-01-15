m = []
def F(n):
    st = ""
    while n!=0:
        st = str(n%3)+st
        n=n//3
    return st
for N in range(1, 50000):
    st = F(N)
    if N%5==0:
        st = st+st[-2:]
    else:
        st = st + F((N%5)*7)
    R = int(st,3)
    if R < 200:
        m.append(N)
print(sum(m)/len(m))