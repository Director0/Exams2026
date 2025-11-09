def p(n):
    m1 = 0
    pr = 1
    while n>0:
        ost = n%10
        if ost%2==0:
            pr*=ost
        n = n//10
    return pr

a = [int(x) for x in open('17-1.txt')]
k = 0
maxx = 0

for i in range(len(a)-2):
    pp = p(a[i])*p(a[i+1])*p(a[i+2])
    if pp<= 2*10**9:
        s = str(pp)
        if s[:2]=='11' and '6' in s[2:]:
            k+=1
            maxx = max(maxx,pp)
print(k,maxx)
