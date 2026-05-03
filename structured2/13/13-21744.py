from ipaddress import *

for m in range(31, 1, -1):
    net1 = ip_network(f"95.24.2.9/{m}", False)
    net2 = ip_network(f"95.24.3.10/{m}", False)

    if net1 == net2:
        print(len([x for x in net1 if f"{x:b}".count("0") % 2 == 0]))
        break