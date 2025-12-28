from ipaddress import *

for m1 in range(1, 30 + 1):
    net1 = ip_network(f"157.127.172.56/{m1}", False)
    net2 = ip_network(f"157.127.191.78/{m1}", False)

    if net1 != net2:
        print(m1)
        break