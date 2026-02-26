from ipaddress import *

for m in range(1, 32 + 1):
    n1 = IPv4Address(f"212.154.18.25")
    net2 = ip_network(f"212.154.18.0/{m}", False)

    if n1 in net2:
        print(m, net2.num_addresses - 2)