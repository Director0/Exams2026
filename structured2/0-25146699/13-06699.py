from ipaddress import *

for m in range(1, 31 + 1):
    net1 = ip_network(f"211.115.61.154/{m}", False)
    net2 = ip_network(f"211.115.59.137/{m}", False)

    if net1 == net2 and net1.network_address == net2.network_address:
        print(m)
