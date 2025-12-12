from ipaddress import *

net = ip_network("192.168.76.160/255.255.255.240", 0)
nomer = 0
k = 0

for i in net:
    nomer += 1
    i1 = f"{i:b}"

    if nomer % 2 == 0 and i1[24:33].count("1") % 2 == 0:
        k += 1

print(k - 1)