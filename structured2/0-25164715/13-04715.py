from ipaddress import *

for m in range(1, 32 + 1):
    net1 = ip_network(f"118.187.59.255/{m}", False)
    net2 = ip_network(f"118.187.65.115/{m}", False)

    if net1 == net2:
        print(m)