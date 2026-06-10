from ipaddress import *

for m in range(1, 32):
    net1 = ip_network(f"118.187.59.255/{m}", False)
    net2 = ip_network(f"118.187.65.115/{m}", False)

    if net1 != net2 and net1.network_address != net2.network_address and net1.netmask == net2.netmask:
        print(m)