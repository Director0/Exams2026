from ipaddress import *

for m in range(1, 32 + 1):
    net1 = ip_network(f"117.184.113.45/{m}", False)
    net2 = ip_network(f"117.184.64.0/{m}", False)

    if net1 == net2:
        print(m)