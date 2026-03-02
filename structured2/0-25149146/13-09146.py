from ipaddress import *

net1 = ip_network("112.118.211.25/255.255.254.0", False)

r = []

for x in net1.hosts():
    r.append(x)

print(r.index(IPv4Address("112.118.211.25")) + 1)