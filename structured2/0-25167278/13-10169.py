from ipaddress import *

for m in range(1, 33):
    net1 = ip_network(f"157.127.182.76/{m}", False)
    net2 = ip_network(f"157.127.190.80/{m}", False)

    if net1.network_address != net2.network_address and net1.netmask == net2.netmask:
        print(m)