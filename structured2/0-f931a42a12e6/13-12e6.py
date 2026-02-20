from ipaddress import *

n = ip_network("192.168.0.0/255.255.192.0", False)

print(len([x for x in n if f"{x:b}".count("1") > f"{x:b}".count("1")]))

cnt = 0

for adr in n:
    binadr = f"{adr:b}"

    if binadr.count("1") > binadr.count("0"):
        cnt += 1


print(cnt)