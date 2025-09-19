from ipaddress import *

ip1 = ip_address("216.54.187.235")
ip2 = ip_address("216.54.174.128")

for m1 in range(1, 31):
    net1 = ip_network(f"216.54.187.235/{m1}", False)
    net2 = ip_network(f"216.54.174.128/{m1}", False)

    if net1 != net2 and ip1 not in [net1[0], net1[-1]] and ip2 not in [net2[0], net2[-1]]:
        print(m1)