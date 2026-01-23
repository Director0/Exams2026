from ipaddress import *

for m in range(1, 31 + 1):
    net1 = ip_network(f"111.81.192.0/{m}", False)
    net2 = ip_network(f"111.81.208.27/{m}", False)

    if net1 == net2:
        print(m)