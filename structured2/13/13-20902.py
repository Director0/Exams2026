from ipaddress import *

net = ip_network("172.16.80.0/255.255.248.0", 0)

cnt = 0

for adr in net:
    binadr = f"{adr:b}"

    if binadr.count("1") % 2 != 0:
        cnt += 1

print(cnt)