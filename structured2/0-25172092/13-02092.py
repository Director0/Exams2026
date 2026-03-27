from ipaddress import *

for m in range(1, 33):
    net1 = ip_network(f"193.175.175.231/{m}", False)
    net2 = ip_network(f"193.175.176.118/{m}", False)

    if net1.network_address != net2.network_address and net1.netmask == net2.netmask:
        print(m)